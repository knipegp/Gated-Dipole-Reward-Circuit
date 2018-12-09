import circuit

import tonic_input
import modulated_phasic_input
import input_sum
import modulated_gate
import output
import rectify_output


class ModulatedCircuit(circuit.Circuit):

    def __init__(self,
                 a_rate=5,
                 b_max_level=1,
                 b_reduction_rate=.025,
                 min_reduction=1/20,
                 time_step=.001,
                 steps=1000,
                 tonic_max=1,
                 tonic_min=0,
                 phasic_duty_cycle=.5,
                 phasic_max=10,
                 phasic_min=0):

        self.b_reduction_rate = b_reduction_rate
        self.min_reduction = min_reduction

        super(ModulatedCircuit, self).__init__(a_rate=a_rate,
                                               b_max_level=b_max_level,
                                               time_step=time_step,
                                               steps=steps,
                                               tonic_max=tonic_max,
                                               tonic_min=tonic_min,
                                               phasic_duty_cycle=phasic_duty_cycle,
                                               phasic_max=phasic_max,
                                               phasic_min=phasic_min)

    def init_nodes(self):
        # Init the nodes of a Gated Dipole Circuit
        self.tonic_input = tonic_input.TonicInput(output_max=self.tonic_max,
                                                  output_min=self.tonic_min,
                                                  time_step=self.time_step,
                                                  steps=self.steps)
        self.phasic_input = modulated_phasic_input.ModulatedPhasicInput(min_reduction=self.min_reduction,
                                                                        duty_cycle=self.phasic_duty_cycle,
                                                                        output_max=self.phasic_max,
                                                                        output_min=self.phasic_min,
                                                                        time_step=self.time_step,
                                                                        steps=self.steps)
        self.x1 = input_sum.InputSum(time_step=self.time_step, steps=self.steps)
        self.x2 = input_sum.InputSum(time_step=self.time_step, steps=self.steps)
        self.z1 = modulated_gate.ModulatedGate(a_rate=self.a_rate,
                                               b_max_level=self.b_max_level,
                                               time_step=self.time_step,
                                               steps=self.steps,
                                               b_reduction_rate=self.b_reduction_rate)
        self.z2 = modulated_gate.ModulatedGate(a_rate=self.a_rate,
                                               b_max_level=self.b_max_level,
                                               time_step=self.time_step,
                                               steps=self.steps,
                                               b_reduction_rate=self.b_reduction_rate)
        self.x3 = output.Output(time_step=self.time_step, steps=self.steps)
        self.x4 = output.Output(time_step=self.time_step, steps=self.steps)
        self.x5 = rectify_output.RectifyOutput(time_step=self.time_step, steps=self.steps)
        self.x6 = rectify_output.RectifyOutput(time_step=self.time_step, steps=self.steps)

    def execute(self, runs=1):
        for run_idx in range(1, runs+1):
            # The inputs to the execute methods represent the physical connections between nodes.
            self.tonic_input.execute()
            self.phasic_input.execute(self.x5.output[run_idx-1])
            self.x1.execute(i_input=self.tonic_input.output[run_idx],
                            j_input=self.phasic_input.output[run_idx])
            self.x2.execute(i_input=self.tonic_input.output[run_idx])
            self.z1.execute(s_input=self.x1.output[run_idx], rectify_output_input=self.x5.output[run_idx-1])
            self.z2.execute(s_input=self.x2.output[run_idx], rectify_output_input=self.x6.output[run_idx-1])
            self.x3.execute(s_input=self.x1.output[run_idx], gate_input=self.z1.output[run_idx])
            self.x4.execute(s_input=self.x2.output[run_idx], gate_input=self.z2.output[run_idx])
            self.x5.execute(child_output=self.x3.output[run_idx], opponent_output=self.x4.output[run_idx])
            self.x6.execute(child_output=self.x4.output[run_idx], opponent_output=self.x3.output[run_idx])

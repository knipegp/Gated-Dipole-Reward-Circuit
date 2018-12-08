from matplotlib import pyplot as plt

import tonic_input
import phasic_input
import input_sum
import gate
import output
import rectify_output


class NormalGatedDipole:

    def __init__(self,
                 a_rate=5,
                 b_max_level=1,
                 time_step=.001,
                 steps=1000,
                 tonic_max=1,
                 tonic_min=0,
                 phasic_duty_cycle=.5,
                 phasic_max=10,
                 phasic_min=0):

        # Init constants to be used as parameters for the different nodes and the control of the circuit.
        self.a_rate = a_rate
        self.b_max_level = b_max_level
        self.time_step = time_step
        self.steps = steps
        self.tonic_max = tonic_max
        self.tonic_min = tonic_min
        self.phasic_duty_cycle = phasic_duty_cycle
        self.phasic_max = phasic_max
        self.phasic_min = phasic_min

        # Init the nodes of a Gated Dipole Circuit
        self.tonic_input = tonic_input.TonicInput(output_max=self.tonic_max,
                                                  output_min=self.tonic_min,
                                                  time_step=self.time_step,
                                                  steps=self.steps)
        self.phasic_input = phasic_input.PhasicInput(duty_cycle=self.phasic_duty_cycle,
                                                     output_max=self.phasic_max,
                                                     output_min=self.phasic_min,
                                                     time_step=self.time_step,
                                                     steps=self.steps)
        self.x1 = input_sum.InputSum(time_step=self.time_step, steps=self.steps)
        self.x2 = input_sum.InputSum(time_step=self.time_step, steps=self.steps)
        self.z1 = gate.Gate(a_rate=self.a_rate,
                            b_max_level=self.b_max_level,
                            time_step=self.time_step,
                            steps=self.steps)
        self.z2 = gate.Gate(a_rate=self.a_rate,
                            b_max_level=self.b_max_level,
                            time_step=self.time_step,
                            steps=self.steps)
        self.x3 = output.Output(time_step=self.time_step, steps=self.steps)
        self.x4 = output.Output(time_step=self.time_step, steps=self.steps)
        self.x5 = rectify_output.RectifyOutput(time_step=self.time_step, steps=self.steps)
        self.x6 = rectify_output.RectifyOutput(time_step=self.time_step, steps=self.steps)

    def execute(self, runs=1):
        for run_idx in range(runs):
            for step_idx in range(self.steps):

                # The inputs to the execute methods represent the physical connections between nodes.
                self.tonic_input.execute()
                self.phasic_input.execute()
                self.x1.execute(i_input=self.tonic_input.output[run_idx],
                                j_input=self.phasic_input.output[run_idx])
                self.x2.execute(i_input=self.tonic_input.output[run_idx])
                self.z1.execute(s_input=self.x1.output[run_idx])
                self.z2.execute(s_input=self.x2.output[run_idx])
                self.x3.execute(s_input=self.x1.output[run_idx], gate_input=self.z1.output[run_idx])
                self.x4.execute(s_input=self.x2.output[run_idx], gate_input=self.z2.output[run_idx])
                self.x5.execute(child_output=self.x3.output[run_idx], opponent_output=self.x4.output[run_idx])
                self.x6.execute(child_output=self.x4.output[run_idx], opponent_output=self.x3.output[run_idx])

    def plot(self, run_index=0):
        fig, axs = plt.subplots(5, 2, constrained_layout=True)
        axs[4, 0].plot(self.tonic_input.output[run_index])
        axs[4, 1].plot(self.tonic_input.output[run_index])
        axs[3, 0].plot(self.x1.output[run_index])
        axs[3, 1].plot(self.x2.output[run_index])
        axs[2, 0].plot(self.z1.output[run_index])
        axs[2, 1].plot(self.z2.output[run_index])
        axs[1, 0].plot(self.x3.output[run_index])
        axs[1, 1].plot(self.x4.output[run_index])
        axs[0, 0].plot(self.x5.output[run_index])
        axs[0, 1].plot(self.x6.output[run_index])
        plt.show()

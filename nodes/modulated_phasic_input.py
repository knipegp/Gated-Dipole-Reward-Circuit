import phasic_input
import random


class ModulatedPhasicInput(phasic_input.PhasicInput):

    def __init__(self, min_reduction=1/20, duty_cycle=.5, output_max=10, output_min=-10, time_step=.01, steps=1000):
        super(ModulatedPhasicInput, self).__init__(duty_cycle=duty_cycle,
                                                   output_max=output_max,
                                                   output_min=output_min,
                                                   time_step=time_step,
                                                   steps=steps)
        self.min_reduction = min_reduction
        self.phasic_probability = .5

    def execute(self, rectify_output_input):
        assert len(rectify_output_input) == self.steps, \
            "Length of input and output lists must be consistent."
        # self.output_max = self.output_max - self.min_reduction

        self.calculate_output(self.decision(rectify_output_input))

    def decision(self, rectify_output_input):
        if sum(rectify_output_input) > 0:
            self.phasic_probability = self.phasic_probability + .5/20
        if random.randint(1, 101) < 100*self.phasic_probability + 1:
            return True
        else:
            return False

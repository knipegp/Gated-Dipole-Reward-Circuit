import node
import math


class PhasicInput(node.Node):

    def __init__(self, duty_cycle=.5, output_max=10, output_min=-10, time_step=.01, steps=1000):
        super(PhasicInput, self).__init__(time_step, steps)
        assert 0 < duty_cycle < 1, "Duty cycle must be a ratio between 0 and 1."

        self.output_max = output_max
        self.output_min = output_min
        self.duty_cycle = duty_cycle

    def calculate_output(self):
        steps_high = math.floor(self.steps * self.duty_cycle)
        steps_low = self.steps - steps_high

        self.output.append([self.output_min]*(steps_low//2)
                      + [self.output_max]*steps_high
                      + [self.output_min]*(1000-steps_low//2-steps_high))

    def execute(self):
        self.calculate_output()

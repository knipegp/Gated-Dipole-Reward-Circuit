import operator
from nodes import input_sum


class ModulatedInputSum(input_sum.InputSum):

    def __init__(self, min_reduction=1/10, time_step=.001, steps=1000, add=False):
        super(ModulatedInputSum, self).__init__(time_step, steps)
        self.min_reduction = min_reduction
        self.add = add

    def execute(self, rectify_output_input, i_input, j_input=list()):
        # Determine the S_input to the gate depending on whether a phasic input is being applied to the gate.
        if not j_input:
            assert len(rectify_output_input) == len(i_input) == self.steps, \
                "Length of input and output lists must be consistent."

        else:
            assert len(rectify_output_input) == len(i_input) == len(j_input) == self.steps, \
                "Length of input and output lists must be consistent."
            self.j_input = j_input

        if not self.add and sum(rectify_output_input) > 0:
                self.i_input = list(map(operator.sub, i_input, [self.min_reduction] * self.steps))
                self.min_reduction = self.min_reduction + 1/30
        elif self.add and sum(rectify_output_input) > 0:
            self.i_input = list(map(operator.add, i_input, [self.min_reduction] * self.steps))
            self.min_reduction = self.min_reduction + 1/30
        else:
            self.i_input = i_input

        self.calculate_output()

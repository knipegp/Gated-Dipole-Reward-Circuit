import operator
from nodes import node


class InputSum(node.Node):

    def __init__(self, time_step=.001, steps=1000):
        super(InputSum, self).__init__(time_step, steps)

        self.i_input = self.j_input = [0] * steps

    def calculate_output(self):
        # Element-wise addition of the input lists.
        self.output.append(list(map(operator.add, self.i_input, self.j_input)))

    def execute(self, i_input, j_input=list()):
        # Determine the S_input to the gate depending on whether a phasic input is being applied to the gate.
        if not j_input:
            assert len(i_input) == self.steps, "Length of input and output lists must be consistent."
            self.i_input = i_input
        else:
            assert len(i_input) == len(j_input) == self.steps, "Length of input and output lists must be consistent."
            self.i_input = i_input
            self.j_input = j_input

        self.calculate_output()

from nodes import node
import operator


class Output(node.Node):

    def __init__(self, time_step=.01, steps=1000):
        super(Output, self).__init__(time_step, steps)
        self.s_input = [0] * self.steps
        self.gate_input = [0] * self.steps

    def calculate_output(self):
        self.output.append(list(map(operator.mul, self.s_input, self.gate_input)))

    def execute(self, s_input, gate_input):
        assert len(s_input) == len(gate_input) == self.steps, "Length of input and output lists must be consistent."

        self.s_input = s_input
        self.gate_input = gate_input

        self.calculate_output()

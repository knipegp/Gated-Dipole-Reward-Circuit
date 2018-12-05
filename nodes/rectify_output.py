import node


class RectifyOutput(node.Node):

    def __init__(self, child_output, opponent_output, time_step=.01, steps=1000):
        super(RectifyOutput, self).__init__(time_step, steps)

        self.child_output = [0] * self.steps
        self.opponent_output = [0] * self.steps

    def calculate_output(self):
        for idx in range(self.steps):
            self.output[idx] = self.child_output[idx]-self.opponent_output[idx]
            if self.output[idx] < 0:
                self.output[idx] = 0

    def execute(self, child_output, opponent_output):
        assert len(child_output) == len(opponent_output) == self.steps, \
            "Length of input and output lists must be consistent."

        self.child_output = child_output
        self.opponent_output = opponent_output

        self.calculate_output()
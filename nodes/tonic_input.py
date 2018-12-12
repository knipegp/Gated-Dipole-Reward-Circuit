from nodes import node


class TonicInput(node.Node):

    def __init__(self, output_max=10, output_min=-10, time_step=.01, steps=1000):
        super(TonicInput, self).__init__(time_step, steps)
        self.output_high = output_max
        self.output_low = output_min

    def calculate_output(self):
        self.output.append([self.output_high] * self.steps)

    def execute(self):
        self.calculate_output()

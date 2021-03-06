from nodes import node


class Gate(node.Node):

    def __init__(self, a_rate, b_max_level, time_step=.01, steps=1000):
        super(Gate, self).__init__(time_step, steps)

        self.a_rate = a_rate
        self.b_max_level = b_max_level
        self.s_input = [0] * self.steps

    def calculate_output(self):

        self.output.append([self.a_rate*self.b_max_level / (self.a_rate + self.s_input[0])])

        for idx in range(1, self.steps):
            self.output[len(self.output)-1].append(self.output[len(self.output)-1][idx-1]
                          + self.time_step*(self.a_rate*(self.b_max_level-self.output[len(self.output)-1][idx-1])
                                            - (self.s_input[idx-1]*self.output[len(self.output)-1][idx-1])))

    def execute(self, s_input):
        assert len(s_input) == self.steps, "Length of input and output lists must be consistent."
        self.s_input = s_input

        self.calculate_output()

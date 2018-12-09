import gate


class ModulatedGate(gate.Gate):

    def __init__(self, a_rate, b_max_level, b_reduction_rate=.025, time_step=.01, steps=1000):
        super(ModulatedGate, self).__init__(a_rate=a_rate,
                                            b_max_level=b_max_level,
                                            time_step=time_step,
                                            steps=steps)
        self.b_reduction_rate = b_reduction_rate

    def execute(self, s_input, rectify_output_input):
        assert len(s_input) == self.steps, "Length of input and output lists must be consistent."
        self.s_input = s_input

        # If there was a reward response from the previous use window
        if sum(rectify_output_input) > 0:
            # Reduce the maximum level of avaiable transmitter
            self.b_max_level = self.b_max_level - self.b_reduction_rate

        self.calculate_output()

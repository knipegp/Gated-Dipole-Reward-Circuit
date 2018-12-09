import abc
from matplotlib import pyplot as plt


class Circuit(abc.ABC):

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

        self.tonic_input = None
        self.phasic_input = None
        self.x1 = None
        self.x2 = None
        self.z1 = None
        self.z2 = None
        self.x3 = None
        self.x4 = None
        self.x5 = None
        self.x6 = None
        self.runs = 1

        self.init_nodes()

    @abc.abstractmethod
    def init_nodes(self):
        """

        :param self:
        :return:
        """

    @abc.abstractmethod
    def execute(self):
        """

        :return:
        """

    def plot(self, run_index=(0, )):

        if type(run_index) != list:
            run_index = [run_index]

        fig, axs = plt.subplots(5, 2, constrained_layout=True)

        for single_idx in run_index:
            for idx in self.run_index_generator(single_idx):
                if sum(self.phasic_input.output[idx])\
                        - sum([min(self.phasic_input.output[idx])] * self.steps)\
                        <= 0:
                    pass
                else:
                    break

            axs[4, 0].plot(self.phasic_input.output[idx], label='run: {}'.format(str(idx)))
            axs[4, 0].set_title('Phasic Input')
            axs[4, 1].plot(self.tonic_input.output[idx], label='run: {}'.format(str(idx)))
            axs[4, 1].set_title('Tonic Input')
            axs[3, 0].plot(self.x1.output[idx], label='run: {}'.format(str(idx)))
            axs[3, 0].set_title('X1')
            axs[3, 1].plot(self.x2.output[idx], label='run: {}'.format(str(idx)))
            axs[3, 1].set_title('X2')
            axs[2, 0].plot(self.z1.output[idx], label='run: {}'.format(str(idx)))
            axs[2, 0].set_title('Z1')
            axs[2, 1].plot(self.z2.output[idx], label='run: {}'.format(str(idx)))
            axs[2, 1].set_title('Z2')
            axs[1, 0].plot(self.x3.output[idx], label='run: {}'.format(str(idx)))
            axs[1, 0].set_title('X3')
            axs[1, 1].plot(self.x4.output[idx], label='run: {}'.format(str(idx)))
            axs[1, 1].set_title('X4')
            axs[0, 0].plot(self.x5.output[idx], label='run: {}'.format(str(idx)))
            axs[0, 0].set_title('X5')
            axs[0, 1].plot(self.x6.output[idx], label='run: {}'.format(str(idx)))
            axs[0, 1].set_title('X6')

        plt.legend(loc=0)
        plt.show()

    def run_index_generator(self, run_index):
        if run_index >= len(self.phasic_input.output)-1:
            for idx in range(len(self.phasic_input.output)-1, 0, -1):
                yield idx
        else:
            for idx in range(run_index, len(self.phasic_input.output)-1):
                yield idx

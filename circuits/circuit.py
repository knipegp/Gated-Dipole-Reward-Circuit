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

    def plot(self, run_index=0):
        fig, axs = plt.subplots(5, 2, constrained_layout=True)
        axs[4, 0].plot(self.phasic_input.output[run_index])
        axs[4, 1].plot(self.tonic_input.output[run_index])
        axs[3, 0].plot(self.x1.output[run_index])
        axs[3, 1].plot(self.x2.output[run_index])
        axs[2, 0].plot(self.z1.output[run_index])
        axs[2, 1].plot(self.z2.output[run_index])
        axs[1, 0].plot(self.x3.output[run_index])
        axs[1, 1].plot(self.x4.output[run_index])
        axs[0, 0].plot(self.x5.output[run_index])
        axs[0, 1].plot(self.x6.output[run_index])
        plt.show()

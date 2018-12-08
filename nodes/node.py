import abc


class Node(abc.ABC):

    def __init__(self, time_step=.01, steps=1000):
        self.time_step = time_step
        self.steps = steps

        self.output = list()

    @abc.abstractmethod
    def calculate_output(self):
        """Calculate the output and append to the output list for the given number of steps"""

    @abc.abstractmethod
    def execute(self):
        """Update the inputs to the node and calculate a new list of outputs"""

from collections import deque
from abc import ABC, abstractmethod

class Scheduler(ABC):
    """
    Describes a scheduling algorithm and keeps track of the statistics
    concerned for evaluation.
    """

    msg_warn = 'Scheduler internal state not fresh - are you sure you \
        performed a reset?'

    def __init__(self):
        self.processes = 0
        self.current_time = 0
        self.waiting_time = 0

        # Ready Queue
        self.q = deque()

        # Current running task
        self.active = None

        # Ordered tasks
        ordered = deque()

    @abstractmethod
    def schedule(self, processes):
        """
        Given processes, schedule the order for processes to run. To be
        implemented as a concrete method by child classes.

        Returns a list of tuples: (time, Process)
        """
        assert isinstance(processes, list)

        if self.processes > 0 or self.current_time > 0 or self.waiting_time > 0:
            print(msg_warn)

        self.processes = len(processes)

    def reset(self):
        """Resets the scheulder's internal state."""
        self.processes = 0
        self.current_time = 0
        self.waiting_time = 0

    def step(self):
        """Performs a single step in time."""

        # Increment time
        self.current_time += 1

        # Decrement burst time for the active task (if there is one)
        if self.active:
            self.active.burst_time -= 1

        # Update waiting time
        for process in self.q:
            self.waiting_time += 1

    @property
    def avg_waiting_time(self):
        """Returns the average waiting time of a schedule."""
        return round(float(self.waiting_time) / self.processes, 2)

    def __repr__(self):
        """Return the scheduler's statistics as a string."""
        s = ['# processes: {}'.format(self.processes),
             'current time: {}'.format(self.current_time),
             'waiting time: {}'.format(self.waiting_time),
             'avg waiting time: {}'.format(self.avg_waiting_time)]

        return '\n'.join(s)

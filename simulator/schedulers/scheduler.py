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

        # Ready Queue - can be any kind of queue
        self.q = deque()

        # Current running task
        self.active = None

        # Ordered tasks
        self.ordered = deque()

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

        self.ordered, res = deque(processes), []
        while self.q or self.ordered or self.active:
            self.enqueue_new_jobs()
            if self.timer_interrupt():
                prev = self.active
                process = self.perform_schedule()
                if process and process != prev:
                    res += [(self.current_time, process.id)]
            self.step()

        return res

    def reset(self):
        """Resets the scheulder's internal state."""
        self.processes = 0
        self.current_time = 0
        self.waiting_time = 0
        self.q = deque()
        self.active = None
        self.ordered = deque()

    def step(self):
        """Performs a single step in time."""

        # Increment time
        self.current_time += 1

        # Decrement burst time for the active task (if there is one)
        if self.active:
            self.active.burst_time -= 1

        # Update waiting time
        self.waiting_time += len(self.q)

    def enqueue_new_jobs(self):
        """Enqueues new jobs that just came in into the ready queue."""
        while self.ordered and self.ordered[0].arrive_time == self.current_time:
            self.q += [self.ordered.popleft()]

    def timer_interrupt(self):
        """
        Default only interrupts when a task has completed its execution
        time, or when a new tasks come into an idle CPU.
        """
        if not self.active:
            return True

        completed = self.active.burst_time == 0 if self.active else False
        return completed

    @abstractmethod
    def perform_schedule(self):
        """
        The main algorithm for scheduling should be implemented in this method.

        Returns a new process - the next process to be run.
        """
        pass

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

from simulator.scheduler import Scheduler

class RoundRobin(Scheduler):
    """Constant time quantum Round Robin scheduler."""

    def __init__(self, time_quantum):
        self.q = time_quantum

    def schedule(self, processes):
        super(RoundRobin, self).schedule(processes)
        # TODO: Implementation

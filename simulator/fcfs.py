from simulator.scheduler import Scheduler

class FCFS(Scheduler):
    """First Come First Serve (FCFS) scheduler."""

    def __init__(self):
        self.queue = []

    def schedule(self, processes):
        super(FCFS, self).schedule(processes)
        # TODO: Implementation

from simulator.scheduler import Scheduler

class SJF(Scheduler):
    """Shortest Job First (SJF) scheduler."""

    def __init__(self):
        self.queue = []

    def schedule(self, processes):
        super(SJF, self).schedule(processes)
        # TODO: Implementation

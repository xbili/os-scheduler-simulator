from simulator.scheduler import Scheduler

class SRTF(Scheduler):
    """Shortest Remaining Time First (SRTF) scheduler."""

    def __init__(self):
        self.queue = []

    def schedule(self, processes):
        super(SRTF, self).schedule(processes)

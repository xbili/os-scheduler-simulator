import heapq
from collections import deque

from simulator.scheduler import Scheduler

class SJF(Scheduler):
    """Shortest Job First (SJF) scheduler."""
    def __init__(self, alpha=0.5):
        super(SJF, self).__init__()
        self.alpha = alpha

    def schedule(self, processes):
        """
        We make use of a heap to keep track of the task with the longest burst
        time left.
        """
        super(SJF, self).schedule(processes)

        ordered = deque(sorted(processes, key=lambda x: x.arrive_time))
        res, pq = [], []
        while ordered or pq:
            elapsed = 1

            # Push all arrived processes into the ready queue
            while ordered and ordered[0].arrive_time <= self.current_time:
                heapq.heappush(pq, ordered.popleft())

            if pq:
                active = heapq.heappop(pq)
                res += [(self.current_time, active.id)]
                elapsed = active.burst_time
                self.waiting_time += (self.current_time - active.arrive_time)

            self.current_time += elapsed

        return res

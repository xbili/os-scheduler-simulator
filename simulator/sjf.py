import heapq
from collections import deque

from simulator.scheduler import Scheduler

class SJF(Scheduler):
    """Shortest Job First (SJF) scheduler."""

    def schedule(self, processes):
        """
        We make use of a heap to keep track of the task with the longest burst
        time left.
        """
        super(SJF, self).schedule(processes)

        self.processes = len(processes)

        ordered = deque(sorted(processes, key=lambda x: x.arrive_time))
        res, pq = [], []
        while ordered or pq:
            elapsed = 1

            # Push all arrived processes into the ready queue
            while ordered and ordered[0].arrive_time <= current_time:
                heapq.heappush(pq, ordered.popleft())

            if q:
                active = heapq.heappop(pq)
                res += [(self.current_time, active.id)]
                elapsed = active.burst_time
                self.waiting_time += (self.current_time + active.burst_time) -
                    self.arrive_time

            self.current_time += elapsed

        return res

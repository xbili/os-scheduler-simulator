import heapq
from collections import deque

from simulator.pq import PriorityQueue
from simulator.scheduler import Scheduler

class SJF(Scheduler):
    """Shortest Job First (SJF) scheduler."""
    def __init__(self, alpha=0.5):
        super(SJF, self).__init__()
        self.alpha = alpha
        self.pq = PriorityQueue()

    def schedule(self, processes):
        """
        We make use of a heap to keep track of the task with the longest burst
        time left.
        """
        super(SJF, self).schedule(processes)

        ordered, res = deque(processes), []
        while ordered or not self.pq.is_empty():
            elapsed = 1

            # Push all arrived processes into the ready queue
            while ordered and ordered[0].arrive_time <= self.current_time:
                nxt = ordered.popleft()
                self.pq.add(nxt, priority=nxt.burst_time)

            if not self.pq.is_empty():
                active = self.pq.pop()
                res += [(self.current_time, active.id)]
                elapsed = active.burst_time
                self.waiting_time += (self.current_time - active.arrive_time)

            self.current_time += elapsed

        return res

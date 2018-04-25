from collections import deque

from simulator.core.pq import PriorityQueue
from simulator.schedulers.scheduler import Scheduler

class SRTF(Scheduler):
    """
    Shortest Remaining Time First (SRTF) scheduler.

    Think of this as a Shortest Job First (SJF) but pre-emptive.
    """

    def __init__(self):
        super(SRTF, self).__init__()

        # Ready queue
        self.pq = PriorityQueue()

        # Active job
        self.active = None

    def schedule(self, processes):
        super(SRTF, self).schedule(processes)

        ordered, res = deque(processes), []
        while ordered or not self.pq.is_empty():
            # Add tasks that arrives into the ready queue
            while ordered and ordered[0].arrive_time == self.current_time:
                nxt = ordered.popleft()
                self.pq.add(nxt, priority=nxt.burst_time)

            # Handle case where there is no current active task
            if not self.active and not self.pq.is_empty():
                # Set a new job in the ready queue to be active
                self.active = self.pq.pop()
                res += [(self.current_time, self.active.id)]
            elif not self.active:
                # No jobs currently, but still have other jobs queued up for
                # the simulation
                self.current_time += 1
                continue

            # Handle cases for replacing jobs. Either:
            # 1. They have completed execution, or
            # 2. They are being preempted.
            if self.active.burst_time == 0:
                # Load next job
                if not self.pq.is_empty():
                    self.active = self.pq.pop()
                    res += [(self.current_time, self.active.id)]
                else:
                    self.active = None
                    self.current_time += 1
                    continue
            elif not self.pq.is_empty() and self.active.burst_time > self.pq.peek().burst_time:
                # PREEMPT
                new = self.pq.pop()
                self.pq.add(self.active, priority=self.active.burst_time)
                self.active = new
                res += [(self.current_time, new.id)]

            # Burst time should never be negative
            assert self.active.burst_time >= 0

            self.active.burst_time -= 1
            self.current_time += 1

            # Every job in the PQ is waiting
            self.waiting_time += len(self.pq)

        return res

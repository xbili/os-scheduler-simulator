from collections import deque

from simulator.schedulers.scheduler import Scheduler

class RoundRobin(Scheduler):
    """Constant time quantum Round Robin scheduler."""

    def __init__(self, time_quantum):
        super(RoundRobin, self).__init__()

        self.time_q = time_quantum

        # We make use of a deque to keep track of the ready queue
        self.q = deque()

        # Current running task
        self.active = None

    def schedule(self, processes):
        super(RoundRobin, self).schedule(processes)

        ordered = deque(processes)

        # Keep running round robin until either we run out of processes
        res = []
        self.q += [ordered.popleft()]
        while self.q or ordered:
            # Check if there are any more tasks that should come into the
            # ready queue.
            while ordered and ordered[0].arrive_time <= self.current_time:
                self.q += [ordered.popleft()]

            elapsed = self.time_q

            if self.active:
                if self.active.burst_time <= self.time_q:
                    elapsed = self.active.burst_time
                    self.active = None
                else:
                    self.active.burst_time -= self.time_q

            if self.q:
                if self.active:
                    self.q += [self.active]
                self.active = self.q.popleft()

                res += [(self.current_time, self.active.id)]

            for p in self.q:
                self.waiting_time += elapsed

            self.current_time += elapsed

        return res

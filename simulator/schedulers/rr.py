from collections import deque

from simulator.schedulers.scheduler import Scheduler

class RoundRobin(Scheduler):
    """Constant time quantum Round Robin scheduler."""

    def __init__(self, time_quantum):
        super(RoundRobin, self).__init__()

        self.time_q = time_quantum

        # We make use of a deque to keep track of the ready queue
        self.q = deque()

    def schedule(self, processes):
        super(RoundRobin, self).schedule(processes)

        # Sort the tasks in reverse order so that we can pop tasks off
        ordered = list(reversed(sorted(processes, key=lambda x: -x.arrive_time)))

        # Keep running round robin until either we run out of processes
        res = []
        self.q += [ordered.pop()]
        while self.q or ordered:
            # Check if there are any more tasks that should come into the
            # ready queue.
            while ordered and ordered[-1].arrive_time <= self.current_time:
                self.q += [ordered.pop()]

            elapsed = self.time_q

            if self.q:
                # Take the next element in the ready queue
                nxt = self.q.popleft()

                res += [(self.current_time, nxt.id)]

                if nxt.burst_time > self.time_q:
                    # Decrement the burst time
                    nxt.burst_time -= self.time_q

                    # Add it back into the queue
                    self.q += [nxt]
                else:
                    elapsed = nxt.burst_time

                # Update waiting time
                for process in self.q:
                    if process.id != nxt.id:
                        self.waiting_time += elapsed

            self.current_time += elapsed

        return res

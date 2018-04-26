from collections import deque

from simulator.schedulers.scheduler import Scheduler

class RoundRobin(Scheduler):
    """Constant time quantum Round Robin scheduler."""

    def __init__(self, time_quantum):
        super(RoundRobin, self).__init__()

        # Constant time quantum
        self.time_q = time_quantum

        # Tracks the current interval in a time quantum
        self.curr_q = 0

    def schedule(self, processes):
        super(RoundRobin, self).schedule(processes)

        # Queue up all processes
        self.ordered = deque(processes)

        res = []
        while self.q or self.ordered or self.active:
            self.enqueue_new_jobs()
            if self.timer_interrupt():
                process = self.perform_schedule()
                if process:
                    res += [(self.current_time, process.id)]
            self.step()

        return res

    def perform_schedule(self):
        """
        Returns the next job to execute in the round robin algorithm.

        In this case we simply take the next item in the queue to be the new
        active queue (if there exist one) and push the active item back into
        the queue.
        """
        # No active current job
        if not self.active:
            if self.q:
                self.active = self.q.popleft()
            return self.active

        # Active job still have yet to complete
        if self.active.burst_time > 0:
            self.q += [self.active]

        # Get next
        if self.q:
            nxt = self.q.popleft()
        else:
            nxt = None
        self.curr_q = 0
        self.active = nxt

        return nxt

    def timer_interrupt(self):
        """
        Timer interrupts only when the current active task has ran out of
        its time quantum or has stopped execution.
        """
        depleted = self.curr_q == 0
        stopped = self.active.burst_time == 0 if self.active else False

        return depleted or stopped

    def step(self):
        super(RoundRobin, self).step()

        self.curr_q = (self.curr_q + 1) % self.time_q

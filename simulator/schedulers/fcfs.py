from collections import deque

from simulator.schedulers.scheduler import Scheduler

class FCFS(Scheduler):
    """First Come First Serve (FCFS) scheduler."""

    def __init__(self):
        super(FCFS, self).__init__()

    def schedule(self, processes):
        super(FCFS, self).schedule(processes)

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
        We simply sort the processes by the time that they come in by, and
        only change process as the processes finish their execution on the
        CPU.
        """
        # No active current job
        if not self.active:
            if self.q:
                self.active = self.q.popleft()
            return self.active

        # Get next
        if self.q:
            nxt = self.q.popleft()
        else:
            nxt = None

        self.active = nxt
        return nxt

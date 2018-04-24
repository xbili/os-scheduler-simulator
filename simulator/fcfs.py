from simulator.scheduler import Scheduler

class FCFS(Scheduler):
    """First Come First Serve (FCFS) scheduler."""

    def __init__(self):
        super(FCFS, self).__init__()

    def schedule(self, processes):
        """
        We simply sort the processes by the time that they come in by, and
        only change process as the processes finish their execution on the
        CPU.
        """
        super(FCFS, self).schedule(processes)

        # Sort by the order that they came in
        ordered = sorted(processes, key=lambda x: x.arrive_time)

        res = []
        for idx, process in enumerate(ordered):
            self.processes += 1

            if self.current_time < process.arrive_time:
                self.current_time = process.arrive_time

            # Output current time and next pid
            res += [(self.current_time, process.id)]
            self.waiting_time += self.current_time - process.arrive_time
            self.current_time += process.burst_time

        return res

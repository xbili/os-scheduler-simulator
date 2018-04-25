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

        tau = {process.id: 0 for process in processes}
        ordered, res = deque(processes), []
        prev_burst = 0
        while ordered or not self.pq.is_empty():
            elapsed = 1

            # Push all arrived processes into the ready queue
            while ordered and ordered[0].arrive_time <= self.current_time:
                nxt = ordered.popleft()

                # Predict the next CPU burst for this process
                prediction = self.predict_next_burst(tau[nxt.id], nxt.burst_time)
                tau[nxt.id] = prediction

                self.pq.add(nxt, priority=prediction)

            if not self.pq.is_empty():
                active = self.pq.pop()
                res += [(self.current_time, active.id)]
                elapsed = active.burst_time
                curr_burst = active.burst_time
                self.waiting_time += (self.current_time - active.arrive_time)

            self.current_time += elapsed

        return res

    def predict_next_burst(self, current_prediction, current_burst_time):
        return self.alpha * current_burst_time +\
            (1-self.alpha) * current_prediction

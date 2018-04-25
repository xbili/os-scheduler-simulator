import heapq
import itertools

REMOVED = '<removed-task>'

class PriorityQueue(object):
    """Abstract implementation of a PriorityQueue."""

    def __init__(self):
        self.pq = []
        self.entry_finder = {}
        self.counter = itertools.count()

    def add(self, task, priority=0):
        if task in self.entry_finder:
            self.remove(task)

        count = next(self.counter)
        entry = [priority, count, task]
        self.entry_finder[task] = entry
        heapq.heappush(self.pq, entry)

    def remove(self, task):
        entry = self.entry_finder.pop(task)
        entry[-1] = REMOVED

    def pop(self):
        while self.pq:
            priority, count, task = heapq.heappop(self.pq)
            if task is not REMOVED:
                del self.entry_finder[task]
                return task

        raise KeyError('pop from empty priority queue')

    def is_empty(self):
        return len(self.pq) == 0

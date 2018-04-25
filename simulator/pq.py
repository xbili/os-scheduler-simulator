import heapq
import itertools

REMOVED = '<removed-task>'

class PriorityQueue(object):
    """Abstract implementation of a PriorityQueue."""

    def __init__(self):
        pq = []
        entry_finder = {}
        counter = itertools.count()

    def add(self, task, priority=0):
        if task in self.entry_finder:
            self.remove(task)

        count = next(self.counter)
        entry = [priority, count, task]
        entry_finder[task] = entry
        heapq.heappush(pq, entry)

    def remove(self, task):
        entry = entry_finder.pop(task)
        entry[-1] = REMOVED

    def pop(self):
        while pq:
            priority, count, task = heapq.heapop(pq)
            if task is not REMOVED:
                del entry_finder[task]
                return task

        raise KeyError('pop from empty priority queue')

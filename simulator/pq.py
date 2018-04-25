import heapq
import itertools

REMOVED = '<removed-task>'

class PriorityQueue(object):
    """Implementation of a PriorityQueue. Implemented as a min-heap"""

    def __init__(self):
        self.pq = []
        self.entry_finder = {}
        self.counter = itertools.count()

    def __len__(self):
        """Returns the size of the priority queue"""
        return len(self.entry_finder.keys())

    def add(self, task, priority=0):
        """Adds an entry into priority queue with a specified priority."""
        if task in self.entry_finder:
            self.remove(task)

        count = next(self.counter)
        entry = [priority, count, task]
        self.entry_finder[task] = entry
        heapq.heappush(self.pq, entry)

    def remove(self, task):
        """Removes an entry from the priority queue."""
        entry = self.entry_finder.pop(task)
        entry[-1] = REMOVED

    def pop(self):
        """Removes the smallest element in the priority queue."""
        while self.pq:
            priority, count, task = heapq.heappop(self.pq)
            if task is not REMOVED:
                del self.entry_finder[task]
                return task

        raise KeyError('pop from empty priority queue')

    def peek(self):
        """
        Returns, but doesn't remove the smallest element in the priority
        queue.
        """
        if self.is_empty():
            return None

        return self.pq[0][2]

    def is_empty(self):
        """Returns true if the priority queue is empty."""
        return len(self.entry_finder) == 0

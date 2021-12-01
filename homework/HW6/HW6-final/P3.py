from random import sample
from time import time
from P2 import Heap, MinHeap, MaxHeap
import heapq

class PriorityQueue:
    def __init__(self, max_size):
        self.elements = []
        self.max_size = max_size

    def __len__(self):
        return len(self.elements)

    def __bool__(self):
        return len(self.elements) > 0

    def put(self, val):
        raise NotImplementedError # TODO

    def get(self):
        raise NotImplementedError # TODO

    def peek(self):
        raise NotImplementedError # TODO


class NaivePriorityQueue(PriorityQueue):
    def __init__(self, max_size):
        self.elements = []
        self.max_size = max_size

    def put(self, val):
        if len(self.elements) >= self.max_size:
            raise IndexError("list index out of range")
        else:
            self.elements.append(val)

    def get(self):
        if len(self.elements) == 0:
            raise IndexError("list index out of range")
        else:
            m = min(self.elements)
            self.elements.remove(m)
            return m

    def peek(self):
        if len(self.elements) == 0:
            raise IndexError("list index out of range")
        else:
            return min(self.elements)


class HeapPriorityQueue(PriorityQueue):
    def __init__(self, max_size):
        self.elements = []
        self.max_size = max_size
        self.heap = MinHeap(self.elements)

    def put(self, val):
        if len(self.elements) >= self.max_size:
            raise IndexError("list index out of range")
        else:
            self.heap.heappush(val)

    def get(self):
        if len(self.elements) == 0:
            raise IndexError("list index out of range")
        else:
            return self.heap.heappop()

    def peek(self):
        if len(self.elements) == 0:
            raise IndexError("list index out of range")
        else:
            return self.heap.elements[0]


class PythonHeapPriorityQueue(PriorityQueue):
    def __init__(self, max_size):
        self.elements = []
        self.max_size = max_size

    def put(self, val):
        if len(self.elements) >= self.max_size:
            raise IndexError("list index out of range")
        else:
            self.elements.append(val)
            heapq.heapify(self.elements)

    def get(self):
        if len(self.elements) == 0:
            raise IndexError("list index out of range")
        else:
            return heapq.heappop(self.elements)

    def peek(self):
        if len(self.elements) == 0:
            raise IndexError("list index out of range")
        else:
            return self.elements[0]

if __name__ == "__main__":
    q = PythonHeapPriorityQueue(2)
    q.put(1)
    q.put(2)
    print(q.elements)
    print(q.peek())
    print(q.elements)
    print(q.get())
    print(q.elements)
    print(q.get())

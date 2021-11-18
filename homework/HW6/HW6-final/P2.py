from math import floor
from typing import List

class Heap:
    def __init__(self, array: List[int]) -> None:
        self.elements = array
        self.size = len(array) # Number of elements in heap
        self.build_heap()

    # index of left child of the node at idx
    def left(self, idx: int) -> int:
        return 2 * idx + 1

    # index of right child of the node at idx
    def right(self, idx: int) -> int:
        return 2 * idx + 2

    def parent(self, idx: int) -> int:
        return floor((idx - 1) / 2)

    def swap(self, idx1: int, idx2: int) -> None:
        tmp = self.elements[idx1]
        self.elements[idx1] = self.elements[idx2]
        self.elements[idx2] = tmp

    def to_string(self, prefix: str = "", idx: int = 0, left: bool = False) -> str:
        if self.size == 0:
            return '\\--'
        elif idx < self.size:
            buf = prefix
            if left:
                buf = buf + "|-- "
            else:
                buf = buf + "\\-- "
            buf = buf + '\033[1m' + str(self.elements[idx]) + '\033[0m' + '\n'
            #buf = buf + str(self.elements[idx]) + '\n' #use if above doesn't work

            new_prefix = prefix
            if left:
                new_prefix = new_prefix + "|   "
            else:
                new_prefix = new_prefix + "    "

            return buf + \
                    self.to_string(new_prefix, self.left(idx), True) + \
                    self.to_string(new_prefix, self.right(idx), False)
        else:
            return ''

    def __str__(self) -> str:
        return self.to_string()

    def __len__(self) -> int:
        return self.size

    # TODO: override this in your dervied classes
    def compare(self, a: int, b: int) -> bool:
        raise NotImplementedError

    def heapify(self, idx: int) -> None:
        # TODO: your solution from the previous question can go here
        #       but remember to use your new "self.compare(a, b)" instead
        #       of raw comparisons
        left = 2*idx+1
        right = 2*idx+2
        cur = self.elements[idx]
        # Violates heap property
        if left < self.size and self.compare(self.elements[left], cur):
            root = left
        else:
            root = idx
        if right < self.size and self.compare(self.elements[right], self.elements[root]):
            root = right
        if root != idx:
            self.swap(idx, root)
            self.heapify(root)


    def build_heap(self) -> None:
        # TODO: your solution from the previous question can go here
        n = int((self.size // 2)-1)
        for i in range(n, -1, -1):
            self.heapify(i)

    def heappush(self, key: int) -> None:
        # TODO: your solution from the previous question can go here
        #       but remember to use your new "self.compare(a, b)" instead
        #       of raw comparisons
        self.elements.append(key)
        self.size += 1
        cur = self.size - 1
        while self.compare(self.elements[cur], self.elements[cur//2]):
            self.swap(cur, cur//2)
            cur = int(cur//2)


    def heappop(self) -> int:
        # TODO: your solution from the previous question can go here
        pop = self.elements[0]
        self.elements[0] = self.elements[self.size-1]
        self.size -= 1
        self.elements.pop()
        if self.size > 0:
            self.heapify(0)
        return pop

class MinHeap(Heap):
    # TODO: complete implementation
    def __init__(self, array: List[int]) -> None:
        self.elements = array
        self.size = len(array) # Number of elements in heap
        self.build_heap()

    # return True if a < b
    def compare(self, a, b):
        if a < b:
            return True
        return False

class MaxHeap(Heap):
    # TODO: complete implementation
    def __init__(self, array: List[int]) -> None:
        self.elements = array
        self.size = len(array) # Number of elements in heap
        self.build_heap()

    # return True if a > b
    def compare(self, a, b):
        if a > b:
            return True
        return False



if __name__ == "__main__":
    mn = MinHeap([1,2,3,4,5])
    mx = MaxHeap([1,2,3,4,5])

    print(mn)
    print(mx)

    mn.heappop()
    print(mn)
    mn.heappush(1)
    print(mn)

    mx.heappop()
    print(mx)
    mx.heappush(5)
    print(mx)

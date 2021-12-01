from random import sample
from time import time
from P3 import PriorityQueue, NaivePriorityQueue, HeapPriorityQueue, PythonHeapPriorityQueue
import heapq
import matplotlib.pyplot as plt


def mergesortedlists(lists, pqclass=PriorityQueue):
    merged = []
    pq = pqclass(len(lists))
    for i, l in enumerate(lists):
        pq.put((l.pop(0), i))

    while pq:
        ele, i = pq.get()
        merged.append(ele)
        if lists[i]:
            pq.put((lists[i].pop(0), i))

    return merged


def generatelists(n, length=20, dictionary_path='words.txt'):
    with open(dictionary_path, 'r') as f:
        words = [w.strip() for w in f.readlines()]
    lists = []
    for _ in range(n):
        lists.append(sorted(sample(words, length)))
    return lists


def timeit(ns=(10, 20, 50, 100, 200, 500), pqclass=PriorityQueue, n_average=5):
    elapsed = []
    for n in ns:
        timeaccum = 0
        for _ in range(n_average):
            lists = generatelists(n)
            start = time()
            merged = mergesortedlists(lists, pqclass)
            end   = time()
            timeaccum += end-start
        elapsed.append(timeaccum / n_average)
    return elapsed


if __name__ == "__main__":
    x = [10, 20, 50, 100, 200, 500]
    n_average = 5
    y1 = timeit(x, NaivePriorityQueue, n_average)
    y2 = timeit(x, HeapPriorityQueue, n_average)
    y3 = timeit(x, PythonHeapPriorityQueue, n_average)
    plt.plot(x, y1, x, y2, x, y3)
    plt.legend(["NaivePriorityQueue", "HeapPriorityQueue", "PythonHeapPriorityQueue"])
    plt.xlabel("Number of Lists Merged")
    plt.ylabel('Elapsed Time (sec)')
    plt.title("List Merge Time Performance of Priority Queue Implementations")
    plt.show()

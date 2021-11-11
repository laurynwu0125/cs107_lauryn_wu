
class FibonacciIterator:

    def __init__(self, n):
        self.n = n
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < 0:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        self.n -= 1
        return self.a


class Fibonacci:

    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return FibonacciIterator(self.n)


if __name__ == "__main__":
    fib = Fibonacci(10) # Create a Fibonacci iterator called fib that contains 10 terms
    print(list(iter(fib))) # Iterate over the iterator and create a list.

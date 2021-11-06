

class AutoDiffToy:
    def __init__(self, a, der=1):
        self.val = a
        self.der = der

    def setDev(self, d):
        self.der = d

    def __add__(self, other):
        # if other is an AutoDiffToy
        try:
            return AutoDiffToy(self.val + other.val, self.der + other.der)
        # if other isn't an AutoDiffToy
        except AttributeError:
            o = AutoDiffToy(other, 0)
            return AutoDiffToy(self.val + o.val, self.der + o.der)


    def __radd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        # if both objects are AutoDiffToys, then proceed normally
        try:
            return AutoDiffToy(self.val * other.val, self.der * other.val + other.der * self.val)
        # if other isn't an AutoDiffToy
        except AttributeError:
            o = AutoDiffToy(other, 0)
            return AutoDiffToy(self.val * o.val, self.der * o.val + o.der * self.val)

    def __rmul__(self, other):
        return self.__mul__(other)




if __name__ == "__main__":
    a = 2.0 # Value to evaluate at
    x = AutoDiffToy(a)
    alpha = 2.0
    beta = 3.0

    f = alpha * x + beta
    print(f.val, f.der)

    f = x * alpha + beta
    print(f.val, f.der)

    f = beta + alpha * x
    print(f.val, f.der)

    f = beta + x * alpha
    print(f.val, f.der)

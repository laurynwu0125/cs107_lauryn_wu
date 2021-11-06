import matplotlib.pyplot as plt
import math
import numpy as np

def numerical_diff(f, h):
    def inner(x):
        return (f(x+h) - f(x)) / h

    return inner

if __name__ == "__main__":
    f = math.log
    exps = [-1, -7, -15]
    x = np.arange(2, 4, 0.02)
    derivs = np.array(1/x)
    plt.plot(x, derivs, linewidth=1)

    for ex in exps:
        diff = numerical_diff(f, 10**ex)
        applyFunc = np.vectorize(diff)
        derivs = applyFunc(x)
        plt.plot(x, derivs, linewidth=1)

    plt.legend(["analytical derivative", r'$h=10^{-1}$', r'$h=10^{-7}$', r'$h=10^{-15}$'])
    plt.xlabel(r'$x$')
    plt.ylabel('Derivative')
    plt.title('Finite Difference and True Derivative Performance')

    qa = "Answer to Q-a: The value of h that most closely approximates the true derivative is 10^(-7). When h is too small, the program is unable to handle the arithmetic of such small numbers. When h is too large, it does not approximate the derivative accurately."
    qb = "Answer to Q-b: AD addresses these issues, because it splits the computation into steps performing elementary operations, so the program can compute the derivatives accurately without overflowing. It removes any errors that may arise from complex computations that the computer can't handle all at once."
    print(qa)
    print(qb)



    plt.show()

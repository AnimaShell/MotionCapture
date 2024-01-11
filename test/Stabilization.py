import random
import matplotlib.pyplot as plt
import numpy as np

stabilize_size = 10


def actionStabilize(data, size):
    stabilizeQueue = []
    ans = []

    for value in data:
        stabilizeQueue.append(value)
        if len(stabilizeQueue) > 2 * size + 1:
            stabilizeQueue.pop(0)
        if len(stabilizeQueue) > size:
            ans.append(np.mean(stabilizeQueue))

    return ans


if __name__ == "__main__":
    d = [np.sin(i / 100) * 10 + random.random() for i in range(1000)]
    ast = d.copy()
    ast = actionStabilize(ast, stabilize_size)
    plt.plot(d, marker="o", linestyle="", color="g")
    plt.plot(ast, linestyle="-", color="r")
    plt.show()

import math

import numpy as np
from matplotlib import pyplot as plt

from task_2.golden_hord import Method


def dfx1(x1: float, x2: float) -> float:
    return 4 * x1 + 4 * math.pow(x2, 3) - 10 * x2


def dfx2(x1: float, x2: float) -> float:
    return 12 * x1 * math.pow(x2, 2) - 10 * x1 + 2 * x2


def fy(y: float) -> float:
    return -12 / 4 * math.pow(y, 5) + 106 / 4 * math.pow(y, 3) + 122 / 4 * y


X = np.arange(-25, 25, 0.001)
Y = [fy(i) for i in X]

plt.ylim(-2, 2)
plt.xlim(-5, 5)
plt.plot(X, [0 for _ in X], color="r")
plt.plot([0 for _ in X], X, color="r")
plt.plot(X, Y)
plt.show()

print(Method(-4, -3, fy))

print(Method(-1, 1, fy))

print(Method(2, 4, fy))

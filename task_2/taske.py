import math

import numpy as np
from matplotlib import pyplot as plt

from golden_hord import Method
from hesse import *


def dfx1(x1: float, x2: float) -> float:
    return 4 * x1 + 4 * math.pow(x2, 3) - 10 * x2


def dfx2(x1: float, x2: float) -> float:
    return 12 * x1 * math.pow(x2, 2) - 10 * x1 + 2 * x2


def xfy(y: float) -> float:
    return -math.pow(y, 3) + 2.5 * y


def fy(y: float) -> float:
    return -12 * math.pow(y, 5) + 40 * math.pow(y, 3) - 23 * y


X = np.arange(-25, 25, 0.001)
Y = [fy(i) for i in X]

plt.ylim(-2, 2)
plt.xlim(-2, 2)
plt.plot(X, [0 for _ in X], color="r")
plt.plot([0 for _ in X], X, color="r")
plt.plot(X, Y)
plt.show()

yn: list[float] = []
print("первый корень")
yn.append(Method(-2, -1.5, fy))
print(yn[0])
print("второй корень")
yn.append(Method(-1, 0.7, fy))
print(yn[1])
print("третий корень")
yn.append(Method(0, 0.5, fy))
print(yn[2])
print("четвертый корень")
yn.append(Method(0.5, 1, fy))
print(yn[3])
print("пятый корень")
yn.append(Method(1.4, 2, fy))
print(yn[4])

dots: list[tuple[float, float]] = [(0, 0) for _ in range(len(yn))]

for i, yi in enumerate(yn):
    dots[i] = (xfy(yi), yi)

ti = TwoIndependent()

extremes = ti.list_extremes(dots, hesse_matrix_zero)

for i, val in enumerate(dots):
    print(f"В точке D({val[0]},{val[1]}) функция {extremes[i]}")

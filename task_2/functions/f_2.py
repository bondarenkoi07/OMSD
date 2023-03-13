"""
f(𝑥, 𝑦) = 𝑥^2 + 𝑥𝑦 + 𝑦^2 − 4 ln 𝑥 − 10 ln 𝑦

dfx: 2x + y - 4/x = 0
dfy: x + 2y - 10/y = 0

x =10/y - 2y

20/y - 4y + y - 4/(10/y-2y) = 20/y -3y - 4(10/y - 2y) = 0

"""
import math

import numpy as np
from matplotlib import pyplot as plt

from task_2.golden_hord import Method
from task_2.hesse import TwoIndependent


def diff1(x, y) -> float:
    return 2 + 4 / math.pow(x, 2)


def diff2(x, y) -> float:
    return 1


diff3 = diff2


def diff4(x, y) -> float:
    return 2 + 10 / math.pow(y, 2)


def fy(y: float) -> float:
    return 20 / y - 3 * y - 4 / (10 / y - 2 * y)


def xfy(y: float) -> float:
    return 10 / y - 2 * y


Y = np.arange(0.001, 20, 0.001)
X = [fy(i) for i in Y]

plt.ylim(-4, 4)
plt.xlim(0, 4)
plt.plot(X, [0 for _ in X], color="r")
plt.plot([0 for _ in X], X, color="r")
plt.plot(Y, X)


yn: list[float] = []
print("первый корень")
yn.append(Method(2.2, 2.26, fy))
print(yn[0])
print("второй корень")
yn.append(Method(2, 2.0001, fy))
print(yn[1])
print("третий корень")
yn.append(Method(2.5, 3, fy))
print(yn[2])

for dot in yn:
    plt.plot([dot for _ in X], X, color="g")

plt.show()

dots: list[tuple[float, float]] = [(0, 0) for _ in range(len(yn))]

for i, yi in enumerate(yn):
    dots[i] = (xfy(yi), yi)


hesse_matrix = [[diff1, diff2], [diff3, diff4]]

ti = TwoIndependent()

extremes = ti.list_extremes(dots, hesse_matrix)

for i, val in enumerate(dots):
    print(f"В точке D({val[0]},{val[1]}) функция {extremes[i]}")

"""#
dfx: 2x + 12y = 0| (2, 12, 0)|(0)
dfy: 2y + 12x = 0| (12, 2, 0)|(0)
dfz: 2z = -2     | (0, 0, 2) |(-2)
B = AX
"""
import numpy as np

from task_2.hesse import ThreeIndependent

A = np.matrix([[2, 12, 0], [12, 2, 0], [0, 0, 2]])
B = np.matrix([0, 0, -2])
X: np.matrix = (np.linalg.inv(A) * B.transpose()).transpose()


def d2fx1(x1, x2, x3) -> float:
    return 2


def d2fx2(x1, x2, x3) -> float:
    return 2


def d2fx3(x1, x2, x3) -> float:
    return 2


def dfx1x2(x1, x2, x3) -> float:
    return 12


def dfx2x1(x1, x2, x3) -> float:
    return 12


def dfx3x1(x1, x2, x3) -> float:
    return 0


def dfx3x2(x1, x2, x3) -> float:
    return 0


hesse_matrix: list[list] = [
    [d2fx1, dfx2x1, dfx3x1],
    [dfx1x2, d2fx2, dfx3x2],
    [dfx3x1, dfx3x2, d2fx3],
]

ti = ThreeIndependent()

dots: list[tuple] = [ tuple([X[0, 0], X[0, 1], X[0, 2]]) ]
print(dots)
extremes = ti.list_extremes(dots, hesse_matrix)

for i, val in enumerate(dots):
    print(f"В точке D({val[0]}, {val[1]}, {val[2]}) функция {extremes[i]}")
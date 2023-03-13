"""
dfy: 2*y^3 + 2x^2y - 2y = 0 | : 2y
dfx: 2*x^3 + 2y^2x - 2x = 0  | : 2x

y^2 + x^2 - 1 = x^2 +y^2 -1
0 = 0

E(0, 0)

"""
import math

from task_2.hesse import TwoIndependent


def diff1(x, y) -> float:
    return (
        4 * math.pow(x, 4)
        + (4 * math.pow(y, 2) - 10) * math.pow(x, 2)
        - 2 * math.pow(y, 2)
        + 2
    ) * math.pow(math.e, -math.pow(x, 2) - math.pow(y, 2))


def diff2(x, y) -> float:
    return (4 * y * math.pow(x, 3) + (4 * math.pow(y, 3) - 8 * y) * x) * math.pow(
        math.e, -math.pow(x, 2) - math.pow(y, 2)
    )


diff3 = diff2


def diff4(x, y) -> float:
    return (
        4 * math.pow(y, 4)
        + (4 * math.pow(x, 2) - 10) * math.pow(y, 2)
        - 2 * math.pow(x, 2)
        + 2
    ) * math.pow(math.e, -math.pow(x, 2) - math.pow(y, 2))


hesse_matrix = [[diff1, diff2], [diff3, diff4]]

ti = TwoIndependent()

dots = [(0, 0)]

extremes = ti.list_extremes(dots, hesse_matrix)

for i, val in enumerate(dots):
    print(f"В точке D({val[0]},{val[1]}) функция {extremes[i]}")

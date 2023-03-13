import math
from functools import reduce
from operator import mul

import numpy as np


def diff1(x: float, y: float):
    return 4


def diff2(x: float, y: float):
    return 12 * math.pow(y, 2) - 10


diff3 = diff2


def diff4(x: float, y: float):
    return 24 * x * y + 2


def matrix_minor(arr, i) -> np.matrix:
    return arr[
        np.array(list(range(i)) + list(range(i + 1, arr.shape[0])))[:, np.newaxis],
        np.array(list(range(i)) + list(range(i + 1, arr.shape[1]))),
    ]


hesse_matrix_zero = [[diff1, diff2], [diff3, diff4]]


class TwoIndependent:
    @staticmethod
    def list_extremes(dots, hesse_matrix: list[list]) -> list[str]:
        extremes = ["" for _ in range(len(dots))]
        for i, dot in enumerate(dots):
            minors = []
            hesse = np.matrix(
                [
                    [
                        hesse_matrix[0][0](dot[0], dot[1]),
                        hesse_matrix[0][1](dot[0], dot[1]),
                    ],
                    [
                        hesse_matrix[1][0](dot[0], dot[1]),
                        hesse_matrix[1][1](dot[0], dot[1]),
                    ],
                ]
            )

            for j in range(len(hesse)):
                minors.append(np.linalg.det(matrix_minor(hesse, j)))

            extremes[i] = TwoIndependent().silvester_criteria(minors)

        return extremes

    @staticmethod
    def silvester_criteria(minors: list[int]) -> str:
        power = reduce(mul, minors)
        # print(f"minor={minors}")
        if power > 0:
            return "Положительно определена"

        is_rotated = True

        for i in range(0, len(minors) - 1):
            if minors[i] * minors[i + 1] > 0:
                is_rotated = False
                break

        if is_rotated:
            return "Отрицательно определена"

        if reduce(lambda a, b: a and b, map(lambda x: x >= 0, minors)):
            return "Неотрицательно определена"

        if reduce(lambda a, b: a and b, map(lambda x: x <= 0, minors)):
            return "Неположительно определена"

        return "не имеет экстремума в данной точке"


class ThreeIndependent(TwoIndependent):
    @staticmethod
    def list_extremes(dots, hesse_matrix: list[list]) -> list[str]:
        extremes = ["" for _ in range(len(dots))]
        for i, dot in enumerate(dots):
            minors = []
            hesse = np.matrix(
                [
                    [
                        hesse_matrix[0][0](dot[0], dot[1], dot[2]),
                        hesse_matrix[0][1](dot[0], dot[1], dot[2]),
                        hesse_matrix[0][2](dot[0], dot[1], dot[2]),
                    ],
                    [
                        hesse_matrix[1][0](dot[0], dot[1], dot[2]),
                        hesse_matrix[1][1](dot[0], dot[1], dot[2]),
                        hesse_matrix[1][2](dot[0], dot[1], dot[2]),
                    ],
                    [
                        hesse_matrix[2][0](dot[0], dot[1], dot[2]),
                        hesse_matrix[2][1](dot[0], dot[1], dot[2]),
                        hesse_matrix[2][2](dot[0], dot[1], dot[2]),
                    ],
                ]
            )

            for j in range(len(hesse)):
                minors.append(np.linalg.det(matrix_minor(hesse, j)))

            extremes[i] = TwoIndependent().silvester_criteria(minors)

        return extremes


if __name__ == "__main__":
    matrix = np.matrix([[1, 2], [2, 3]])
    print(matrix_minor(matrix, 0))
    print(matrix_minor(matrix, 2))

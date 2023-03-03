import math


def bisection(f: lambda x: float, a: float, b: float, eps: float, extremum: int = 1) -> tuple[float, float]:
    iteration = 0
    while math.fabs(a - b) > eps:
        x = (a + b) / 2
        print(f"итерация №{iteration+1}, текущее приближение x{iteration}={x}")
        f1 = f(x - eps)
        f2 = f(x + eps)
        if extremum * f1 < extremum * f2:
            b = x
        else:
            a = x
        iteration += 1

    print(f"итоговое приближение x{iteration}={(a + b) / 2}")
    return (a + b) / 2, f((a + b) / 2)

import math


def Method(a, b, f):
    try:
        while math.fabs(a - b) > math.pow(10, -5):
            a = a - (b - a) * f(a) / (f(b) - f(a))
            b = b - (a - b) * f(b) / (f(a) - f(b))
            print(f"текущее приближение b")
        return b
    except ValueError:
        print("Value not invalidate")

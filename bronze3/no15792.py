import sys
from decimal import Decimal


def divide(a, b):
    if len(str(a/b)) <= 2000:
        return a/b
    else:
        return "%.2000f" % (a / b)


A, B = sys.stdin.readline().split()
print(divide(Decimal(A), Decimal(B)))

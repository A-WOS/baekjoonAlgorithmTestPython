from math import gcd


def lcm(x, y):
    return x * y // gcd(x, y)


A, B = map(int, input().split())
print(lcm(A, B))

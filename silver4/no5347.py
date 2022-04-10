from math import gcd


def lcm(x, y):
    return x * y // gcd(x, y)


for _ in range(int(input())):
    a, b = map(int, input().split())
    print(lcm(a, b))

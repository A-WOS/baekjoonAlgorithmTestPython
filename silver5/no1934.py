from math import gcd


def lcm(x, y):
    return x * y // gcd(x, y)


t = int(input())
for _ in range(t):
    A, B = map(int, input().split())
    print(lcm(A, B))

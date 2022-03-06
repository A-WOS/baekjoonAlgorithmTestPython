from math import gcd


def rs_gcd(x, y):
    return x * y // gcd(x, y)


t = int(input())
for _ in range(t):
    A, B = map(int, input().split())
    print(rs_gcd(A, B))

import sys

T = int(sys.stdin.readline().rstrip())
a, b = 0, 0
for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    if A > B:
        a += 1
    elif B > A:
        b += 1

print(a, b)

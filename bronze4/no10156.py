import sys

K, N, M = map(int, sys.stdin.readline().split())
result = K * N - M
if K * N < M:
    result = 0

print(result)

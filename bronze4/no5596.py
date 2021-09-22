import sys
print(max(list(sum(map(int, sys.stdin.readline().split())) for _ in range(2))))
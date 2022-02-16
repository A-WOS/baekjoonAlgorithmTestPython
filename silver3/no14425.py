import sys

N, M = map(int, sys.stdin.readline().split())
S = set()
for _ in range(N):
    S.add(sys.stdin.readline().rstrip())

rs = 0
for _ in range(M):
    word = sys.stdin.readline().rstrip()
    if word in S:
        rs += 1
print(rs)


# Solved #2
# N, M = map(int, input().split())
# S = set()
# rs = 0
# for _ in range(N): S.add(input())
# for _ in range(M):
#     word = input()
#     if word in S: rs += 1
# print(rs)

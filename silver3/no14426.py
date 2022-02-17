import sys

N, M = map(int, sys.stdin.readline().split())
S = set()
rs = 0
for _ in range(N):
    prefix_word = sys.stdin.readline().rstrip()
    for i in range(len(prefix_word)):
        S.add(prefix_word[:i+1])

for _ in range(M):
    word = sys.stdin.readline().rstrip()
    if word in S:
        rs += 1

print(rs)

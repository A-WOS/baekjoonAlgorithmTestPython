import sys

N, M = map(int, sys.stdin.readline().split())
d_list = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

K = int(sys.stdin.readline().rstrip())
for _ in range(K):
    i, j, x, y = map(int, sys.stdin.readline().split())
    # result = 0
    # for a in range(i-1, x):
    #     for b in range(j-1, y):
    #         result += d_list[a][b]
    # print(result)

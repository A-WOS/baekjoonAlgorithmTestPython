N, M = map(int, input().split())
A, B = [], []
for _ in range(N):
    A.append(list(map(int, input().split())))
M, K = map(int, input().split())
for _ in range(M):
    B.append(list(map(int, input().split())))

rs = [[0 for _ in range(K)] for _ in range(N)]
for i in range(N):
    for j in range(K):
        for x in range(M):
            rs[i][j] += A[i][x] * B[x][j]

for i in range(len(rs)):
    print(' '.join(map(str, rs[i])))

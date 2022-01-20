def row_col(n):
    dual_l = [list(map(int, input().split())) for _ in range(n)]
    return dual_l


N, M = map(int, input().split())
a = row_col(N)
b = row_col(N)
sum_l = [['' for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        sum_l[i][j] = str(a[i][j] + b[i][j])

for row in sum_l:
    print(' '.join(row))


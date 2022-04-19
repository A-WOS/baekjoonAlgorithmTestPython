N = int(input())
cnt = 1
for i in range(N):
    r = 2 * N - cnt
    print(f'{" "*i}{"*"*r}')
    cnt += 2

cnt = 3
for i in range(N-2, -1, -1):
    print(f'{" " * i}{"*" * cnt}')
    cnt += 2

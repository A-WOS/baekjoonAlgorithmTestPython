N = int(input())
cnt = 1
for i in range(N-1, -1, -1):
    print(f'{" "*i}{"*"*cnt}')
    cnt += 2

cnt = 1
for i in range(1, N):
    r = 2 * (N-1) - cnt
    print(f'{" "*i}{"*"*r}')
    cnt += 2

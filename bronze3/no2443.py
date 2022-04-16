N = int(input())
cnt = 1
for i in range(N):
    r = 2 * N - cnt
    print(f'{" "*i}{"*"*r}')
    cnt += 2

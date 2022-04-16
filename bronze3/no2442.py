N = int(input())
cnt = 1
for i in range(N-1, -1, -1):
    print(f'{" "*i}{"*"*cnt}')
    cnt += 2

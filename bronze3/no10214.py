T = int(input())
for _ in range(T):
    tot_N, tot_M = 0, 0
    for _ in range(9):
        N, M = map(int, input().split())
        tot_N += N
        tot_M += M
    print('Draw') if tot_N == tot_M else print('Yonsei') if tot_N > tot_M else print('Korea')


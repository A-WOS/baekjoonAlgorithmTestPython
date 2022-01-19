T = True
while T:
    n, m = map(int, input().split())
    if n == m == 0:
        T = False
    else:
        print('Yes') if n > m else print('No')

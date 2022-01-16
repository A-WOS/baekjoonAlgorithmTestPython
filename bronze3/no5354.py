for _ in range(int(input())):
    n = int(input())
    l = [['' for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n-1 or j == 0 or j == n-1:
                l[i][j] = '#'
            else:
                l[i][j] = 'J'

    for val in l:
        print(''.join(val))
    print()

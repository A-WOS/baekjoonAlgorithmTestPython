t = int(input())
for _ in range(t):
    n = input()
    sqr_n = str(int(n)**2)
    print('YES') if n == sqr_n[-len(n):] else print('NO')


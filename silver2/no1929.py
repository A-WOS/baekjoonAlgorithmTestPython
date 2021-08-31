a = 1000000
b = [False, False] + [True] * (a - 1)
sosu = []
for i in range(2, a + 1):
    if b[i]:
        sosu.append(i)
    for j in range(2 * i, a + 1, i):
        b[j] = False

M, N = map(int, input().split())
for i in sosu:
    if M <= i <= N:
        print(i)

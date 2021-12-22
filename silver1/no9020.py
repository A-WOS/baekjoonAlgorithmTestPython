# 2보다 큰 짝수는 두 소수의 합으로 나타낼 수 있다.
n = []
T = int(input())
for _ in range(T):
    n.append(int(input()))

a = [False, False] + [True] * (max(n) - 1)
sosu = []

for i in range(2, max(n) + 1):
    if a[i]:
        sosu.append(i)
    for j in range(2*i, max(n)+1, i):
        a[j] = False

print(n)
print(sosu)

# for i in range(len(sosu))

n = 123456*2
# 0, 1 = False, 소수는 2부터 시작이므로 True 로 설정
a = [False, False] + [True] * (n - 1)
primes = []

for i in range(2, n + 1):
    if a[i]:
        primes.append(i)
        for j in range(2 * i, n + 1, i):
            a[j] = False

while True:
    N = int(input())
    if N == 0:
        break
    cnt = 0
    for i in primes:
        if N < i <= 2 * N:
            cnt += 1
    print(cnt)
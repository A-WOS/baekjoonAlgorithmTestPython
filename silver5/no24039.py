N = int(input())

a = [False, False] + [True] * 102
primes = []

for i in range(2, 104):
    if a[i]:
        primes.append(i)
        for j in range(2 * i, 104, i):
            a[j] = False

rs = [0] * 26
for i in range(len(primes) - 1):
    rs[i] = primes[i] * primes[i + 1]

for num in rs:
    if num > N:
        print(num)
        break

N, K = map(int, input().split())
h = N
m = 59
times = []
for h in range(0, N + 1):
    for m in range(0, 60):
        for s in range(0, 60):
            times.append(list(str(h).zfill(2) + str(m).zfill(2) + str(s).zfill(2)))
tot = 0
for time in times:
    if time.count(str(K)):
        tot += 1
print(tot)

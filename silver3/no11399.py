n = int(input())
times = sorted(map(int,input().split()))
tot = 0
for i in range(len(times)):
    j = 0
    tot += sum(times[j:i+1])
print(tot)
n = int(input())
l1 = list(reversed(sorted(map(int, input().split()))))
l2 = sorted(list(map(int, input().split())))
tot = 0
for i in range(n):
    tot += l1[i] * l2[i]
print(tot)
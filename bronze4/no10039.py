import sys

l = list(int(sys.stdin.readline()) for x in range(5))

for i in range(len(l)):
    if l[i] < 40:
        l[i] = 40

print(int(sum(l) / len(l)))
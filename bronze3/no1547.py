M = int(input())

cup = [1, 0, 0]
for i in range(M):
    x, y = map(int, input().split())

    cup[x - 1], cup[y - 1] = cup[y - 1], cup[x - 1]

for i in range(len(cup)):
    if cup[i] == 1:
        print(i+1)

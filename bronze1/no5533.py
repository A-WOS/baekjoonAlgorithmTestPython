n = int(input())
humans = [[],[],[]]
tot = []
for i in range(n):
    a, b, c = map(int, input().split())
    humans[0].append(a)
    humans[1].append(b)
    humans[2].append(c)

for i in range(n):
    rs = 0
    for j in range(3):
        if humans[j].count(humans[j][i]) == 1:
            rs += humans[j][i]
    tot.append(rs)
for val in tot:
    print(val)

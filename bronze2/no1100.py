l = []
for i in range(8):
    l.append(list(map(str, input())))

count = 0
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0 and l[i][j] == 'F':
            count += 1
print(count)

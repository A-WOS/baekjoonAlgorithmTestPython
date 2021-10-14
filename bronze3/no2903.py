point = [9]
j = 1
for i in range(2, 16):
    j *= 2
    point.append((int(point[i - 2] ** 0.5) + j) ** 2)

# for index, val in enumerate(point):
#     print(index, val)
print(point[int(input()) - 1])

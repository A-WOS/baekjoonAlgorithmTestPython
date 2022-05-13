n = int(input())
q1, q2, q3, q4, axis = 0, 0, 0, 0, 0
Q_dim = [0 for i in range(5)]
for _ in range(n):
    x, y = map(int, input().split())
    if x == 0 or y == 0:
        Q_dim[4] += 1
    elif x > 0 and y > 0:
        Q_dim[0] += 1
    elif x > 0 and y < 0:
        Q_dim[3] += 1
    elif x < 0 and y > 0:
        Q_dim[1] += 1
    elif x < 0 and y < 0:
        Q_dim[2] += 1
for i in range(4):
    print(f'Q{i + 1}: {Q_dim[i]}')
print(f'AXIS: {Q_dim[4]}')

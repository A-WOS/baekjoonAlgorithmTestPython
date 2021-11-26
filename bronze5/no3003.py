chess = [1, 1, 2, 2, 2, 8]
count = list(map(int, input().split()))
for i in range(len(chess)):
    chess[i] -= count[i]

print(' '.join(map(str, chess)))

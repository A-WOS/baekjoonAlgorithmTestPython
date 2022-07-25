n = list(map(int, input().split()))
rs = 0
for i in range(len(n)):
    if n[i] > 0:
        rs += 1
print(rs)
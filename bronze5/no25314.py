n = int(input()) // 4
rs = []
for _ in range(n):
    rs.append('long')
rs.append('int')
print(*rs)
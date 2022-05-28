a, b, c = map(int, input().split())
rs = b - a
print(rs // c + 1) if rs % c else print(rs // c)

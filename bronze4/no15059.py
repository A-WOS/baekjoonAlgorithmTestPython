a, b, c = map(int, input().split())
d, e, f = map(int, input().split())
rs = 0
if d > a: rs += d - a
if e > b: rs += e - b
if f > c: rs += f - c
print(rs)

N, B = input().split()

N = N[::-1]
s = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rs = 0

for i, val in enumerate(N):
    rs += (s.index(val)) * (int(B) ** i)
print(rs)

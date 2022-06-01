r = 1
c = 1
n = int(input())
while r * c < n:
    if r > c:
        c += 1
    else:
        r += 1
print(r, c)

l = list(map(int, input().split()))
r = l[0] * 24 * 60 + l[1] * 60 + l[2] - 16511
if r < 0:
    print(-1)
else:
    print(r)

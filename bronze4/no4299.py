a, b = map(int, input().split())
if a - b < 0 or (a - b) % 2 != 0:
    print(-1)
else:
    r1 = (a + b) // 2
    r2 = a - r1

    print(max(r1, r2), min(r1, r2))

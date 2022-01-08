r, c, n = map(int, input().split())
print((r // n + 1 if r % n else r // n) * (c // n + 1 if c % n else c // n))

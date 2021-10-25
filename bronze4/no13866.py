l = list(map(int, input().split()))
l.sort()

r = min(l) + max(l)
l.pop(3)
l.pop(0)
print(abs(r - sum(l)))
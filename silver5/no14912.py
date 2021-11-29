a, b = map(int, input().split())
l = list(str(x + 1) for x in range(a))
count = 0
for i in l:
    count += i.count(str(b))
print(count)

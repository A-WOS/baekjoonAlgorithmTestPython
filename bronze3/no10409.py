l, t = map(int, input().split())
numbers = list(map(int, input().split()))
cnt = 0
for number in numbers:
    t -= number
    if t < 0:
        break
    cnt += 1
print(cnt)
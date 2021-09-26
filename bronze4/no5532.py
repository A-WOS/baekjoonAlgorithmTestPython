n = list(int(input()) for _ in range(5))
count = 0
while True:
    if n[1] <= 0 and n[2] <= 0:
        break
    n[1] -= n[3]
    n[2] -= n[4]
    count += 1

print(n[0] - count)
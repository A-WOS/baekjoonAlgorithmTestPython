tot = 0
for _ in range(int(input())):
    s, a = map(int, input().split())
    tot += a % s
print(tot)
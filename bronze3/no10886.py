n = int(input())
r1, r2 = 0, 0
for _ in range(n):
    if int(input()) == 0:
        r1 += 1
    else:
        r2 += 1
print('Junhee is not cute!') if r1 > r2 else print('Junhee is cute!')

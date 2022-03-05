E, S, M = map(int, input().split())

tot = 1
a, b, c = 1, 1, 1
while True:
    if a == E and b == S and c == M:
        print(tot)
        break

    a += 1
    b += 1
    c += 1

    if a > 15:
        a = 1
    if b > 28:
        b = 1
    if c > 19:
        c = 1

    tot += 1

def gcd(m, n):
    while n != 0:
        t = m % n
        (m, n) = (n, t)
    return abs(m)


def lcd(m, n):
    gcd_result = gcd(m, n)
    m = int(m / gcd_result)
    n = int(n / gcd_result)

    return m * n * gcd_result


t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(lcd(a, b), gcd(a, b))

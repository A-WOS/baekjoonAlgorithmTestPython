a, b = map(int, input().split())


# 유클리드 호제법
def gcd(m, n):
    while n != 0:
        t = m % n
        (m, n) = (n, t)
    return abs(m)


def lcd(m, n):
    gcd_result = gcd(m, n)
    m = int(m / gcd_result)
    n = int(n / gcd_result)

    return m*n*gcd_result


print(gcd(a, b))
print(lcd(a, b))

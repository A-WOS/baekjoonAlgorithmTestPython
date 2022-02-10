n, m = map(int, input().split(":"))

# 최대공약수
def gcd(a, b):
    while b != 0:
        t = a % b
        (a, b) = (b, t)
    return abs(a)


rs = gcd(n, m)
n, m = int(n / rs), int(m / rs)
print(f"{n}:{m}")

for _ in range(int(input())):
    a, b, c, d, e = map(int, input().split())
    print('$' + '{:0.2f}'.format(a * 350.34 + b * 230.9 + c * 190.55 + d * 125.30 + e * 180.90, 2))

a, b = map(int, input().split())
if a < 0 and b < 0:
    b *= -1
    print(abs(a // b))
    print(a % b)
elif a < 0 and b > 0:
    print(a // b)
    print(a % b)
elif b < 0 and a > 0:
    a *= -1
    print((a // b)*-1)
    print(abs(a % b))
else:
    print(a // b)
    print(a % b)
# a = -7 b= -3
# r = +3q +7
# r = -3q -7
# 6q = -14
# q = 7/3

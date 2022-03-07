a, b, n = map(int, input().split())
sosu = list()
for _ in range(n):
    a = (a - (a // b)*b)*10
    sosu.append(a // b)
print(sosu[n-1])

# rs = format(a/b,'.100f').rstrip('0')[2:]
# if n <= len(rs):
#     print(rs[n-1])
# print(0)

# rs = str(a / b).split('.')[1]
# if 0 < n <= len(rs):
#     print(rs[n-1])
# else:
#     print(0)
# print(rs[n-1]) if rs else print(0)
# else:


# 반례 1, 1, 1 -> 1 / 1 = 0 , 1 0.0
# if len(rs) > 0: print(rs[n - 1])
# else: print(rs)
# if str(a/b).split('.')[1][n-1]:
#     print()
# else:
#     print(str(a/b).split('.')[1])
# print(str(a/b))
# print(str(a/b).split('.')[1])

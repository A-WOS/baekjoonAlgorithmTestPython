a, b, n = map(int, input().split())

sosu = list()
# for i in range(n):
a, b = divmod(a, b)
t = b * 10
x, y = divmod(t, b)
# if i > 0: sosu.append(a)
print(x, y)


# print(a/b)
# sosu = list()
# for _ in range(n):
#     # (25 - (25 // 7)*7)*10 -> 두수를 나눠서 소수를 구하기 위한 방식
#     a = (a - (a // b)*b)*10
#     print(a)
#     sosu.append(a // b)
# print(sosu[n-1])

# a, b, n = map(int, input().split())
# 25/7 = 3.5714285... -> 3, 5714285...
# 설명을 쉽게 하기 위해 str_list로 변수 지정
# str_list = str(a/b).split('.')[1]
# print(str_list[n-1])

# rs = format(a/b,'.100f').rstrip('0')[2:]
# print(rs)
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

# 시간초과
# def recurse(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return recurse(n - 1) + recurse(n - 2)
#
#
# k = int(input())
# print(recurse(k - 1), recurse(k))

k = int(input())
pb = [0] * 46
pb[1], pb[2] = 1, 1
for i in range(3, 46):
    pb[i] = pb[i - 2] + pb[i - 1]
print(pb[k - 1], pb[k])

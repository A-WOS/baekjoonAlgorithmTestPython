import sys

A, B = input().split()
# 시간초과
# result = 0
# for i in A:
#     for j in B:
#         result += int(i) * int(j)
# print(result)
# abc = 123, de = 45
# a*d + a*e + b*d + b*e + c*d + c*e = 28
# (a+b+c+)(d+e) = 28
# 4*7 = 28
result_A, result_B = 0, 0
for i in A:
    result_A += int(i)
for i in B:
    result_B += int(i)
print(result_A * result_B)

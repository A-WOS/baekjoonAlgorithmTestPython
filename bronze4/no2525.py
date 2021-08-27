import math

h, m = map(int, input().split())
increase_m = int(input())

tot = 60*h+m+increase_m
h = math.trunc(tot / 60)
m = math.trunc(tot % 60)

if h >= 24:
    h = h - 24
print(h, m)
# if m+increase_m >= 60:
#     h += 1
#     m = m+increase_m - 60
# else:
#     m = m+increase_m
#
# if h >= 24:
#     h = 0

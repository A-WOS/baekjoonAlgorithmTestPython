# import collections

# dct = {}
# for i in range(int(input())):
#     num = input()
#     if num in dct:
#         dct[num] += 1
#     else:
#         dct.__setitem__(num, 1)
#
# rs = collections.OrderedDict(sorted(dct.items()))
# for val in rs:
#     for _ in range(dct[val]):
#         print(val)
import sys

n = int(input())
num_l = list(0 for val in range(10001))
for _ in range(n):
    k = int(sys.stdin.readline().rstrip())
    num_l[k] += 1

for i in range(len(num_l)):
    if num_l[i]:
        for _ in range(num_l[i]):
            print(i)
    # print(val, num_l[val])
    # if num_l[val] != 0:
    #     for _ in range(num_l[val]):
    #         print(num_l.index(num_l[val]))
    # if val:
    #     print(num_l.index(val), val)
import collections

dc = {}
for _ in range(int(input())):
    ext = input().split('.')[-1]
    if ext in dc:
        dc[ext] += 1
    else:
        dc.__setitem__(ext, 1)
sorted_dc = collections.OrderedDict(sorted(dc.items()))
for val in sorted_dc:
    print(val, dc[val])
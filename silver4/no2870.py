import re

res = list()
for i in range(int(input())):
    s = input()
    for v in re.split('[a-z]', s):
        if v:
            res.append(int(v))
res.sort()
for val in res: print(val)

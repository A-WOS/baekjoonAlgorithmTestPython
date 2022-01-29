dct = dict()
keys = [chr(val) for val in range(65, 91)]
n = 1
for i in keys:
    dct[i] = n
    n += 1

nl = int(input())
s = input()
tot = 0
for i in s:
    tot += dct.get(i)
print(tot)
# print(keys)
# values = [val for val in range(1, 27)]
# dct = dict.fromkeys(keys, values)
# print(dct)
# dict.fromkeys()
# dict.from

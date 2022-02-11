# solved #1
# s = input()
# up_c = [chr(val) for val in range(65, 91)]
# low_c = [chr(val) for val in range(97, 123)]
# rs = ''

# for val in s:
#     if low_c.count(val): rs += up_c[low_c.index(val)]
#     else: rs += low_c[up_c.index(val)]
#
# print(rs)

# solved #2
s = input()
rs = ''
for val in s:
    if val.islower() is False: rs += chr(ord(val) + 32)
    else: rs += chr(ord(val) - 32)

print(rs)
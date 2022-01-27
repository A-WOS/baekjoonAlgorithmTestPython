# print(ord('z'))
s = input()
l = list()
for i in range(97, 123):
    l.append(str(s.count(chr(i))))
print(' '.join(l))

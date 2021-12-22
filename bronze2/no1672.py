import sys

a_n = ['A', 'G', 'C', 'T']
b_n = ['A', 'G', 'C', 'T']
# ab_n = [['' for y in range(4)] for x in range(4)]
# print(ab_n)
# for x, i in enumerate(a_n):
#     for y, j in enumerate(b_n):
#         if i == j:
#             ab_n[x][y] = i
#         elif (i == 'A' and j == 'G') or (i == 'G' and j == 'A'):
#

N = int(sys.stdin.readline())
s = ''.join(list(map(str, reversed(sys.stdin.readline().strip()))))
print(s[0:2])
# print(s.pop(1))
while len(s) > 1:
    if 'AA' == s[0:2] or 'AC' or 'CA' or 'TG' or 'GT':
        s[0] = 'A'
        s[1] = ''
    elif s[0:2] == 'AG' or 'GA' or 'CC':
        s[0] = 'C'
        s[1] = ''
    elif s[0:2] == 'GG' or 'AT' or 'TA':
        s[0] = 'G'
        s[1] = ''
    elif s[0:2] == 'CG' or 'GC' or 'TT':
        s[0] = 'T'
        s[1] = ''
# for i in range(len(s)):
#     if i < len(s) - 1:
#         if s[i:i+2] == s[i]:
#             s[i+1] = ''
#         elif s[i:i+2] == ''
print(s)

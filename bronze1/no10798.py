import sys

s = [list(sys.stdin.readline().rstrip()) for _ in range(5)]
rs = ''
max_len = 0
for val in s:
    if max_len < len(val): max_len = len(val)

for val in s:
    if len(val) != max_len:
        for i in range(len(val), max_len):
            val.append('')

for i in range(len(s[0])):
    for j in range(len(s)):
        rs += s[j][i]

print(rs)

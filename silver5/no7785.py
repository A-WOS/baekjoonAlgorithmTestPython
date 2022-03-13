n = int(input())
in_out = set()
for _ in range(n):
    s = input().split()
    if s[1] == 'enter':
        in_out.add(s[0])
    elif s[1] == 'leave':
        in_out.remove(s[0])

for val in sorted(in_out, reverse=True):
    print(val)

# print(rs)
# for val in set(reversed(sorted(in_out))):
#     print(val)

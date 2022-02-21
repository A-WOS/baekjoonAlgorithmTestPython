s = list(input())
rs = s[0]
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        rs += s[i+1]
print(rs)
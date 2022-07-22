s = input()
rs = 0
for i in range(len(s)):
    rs += (ord(s[i])-64)*(26**(len(s)-i-1))
print(rs)

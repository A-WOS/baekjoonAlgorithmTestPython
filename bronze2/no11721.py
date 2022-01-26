s = input()
r = len(s) // 10
e = len(s) % 10
for i in range(r+1):
    if i == r:
        print(s[10*i:len(s)])
    else:
        print(s[10*i:10*(i+1)])
# for i in range(len(s)):
#     if i % 10:
#         print(''.join(s[i]))
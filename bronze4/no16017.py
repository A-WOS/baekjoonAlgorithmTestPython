a = int(input())
b = int(input())
c = int(input())
d = int(input())

flag = 0
if a == 8 or a == 9:
    if d == 8 or d == 9:
        if b == c:
            flag = 1
if flag == 1:
    print('ignore')
else:
    print('answer')



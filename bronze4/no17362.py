n = int(input())
rs = 0
if n % 8 == 1:
    rs = 1
elif n % 8 == 5:
    rs = 5
elif n % 8 == 0 or n % 8 == 2:
    rs = 2
elif n % 8 == 3 or n % 8 == 7:
    rs = 3
elif n % 8 == 4 or n % 8 == 6:
    rs = 4
print(rs)

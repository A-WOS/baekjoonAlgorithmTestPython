from math import factorial

n = int(input())
rs = 0
for val in str(factorial(n))[::-1]:
    if val != '0':
        break
    else:
        rs += 1
print(rs)
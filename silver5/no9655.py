n = int(input())
a, b = int(n // 3), n % 3
rs = ''
if a % 2:
    rs = 'CY'
else:
    rs = 'SK'

if b == 1:
    print(rs)
else:
    if rs == 'SK':
        rs = 'CY'
    else:
        rs = 'SK'
    print(rs)
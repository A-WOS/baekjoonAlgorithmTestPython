def recurse(a, b):
    s = '0123456789ABCDEF'
    if a < b:
        return str(s[a])
    else:
        return recurse(a // b, b) + str(s[a % b])


m, n = map(int, input().split())
print(recurse(m, n))

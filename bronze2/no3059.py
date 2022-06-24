T = int(input())

for _ in range(T):
    alpha = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z'}
    s = set(list(input()))
    rs = list(alpha.difference(s))
    tot = 0
    for val in rs:
        tot += ord(val)
    print(tot)

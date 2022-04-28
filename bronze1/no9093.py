T = int(input())
for _ in range(T):
    s = list(input().split())
    r = ''
    for val in s:
        r += ''.join(list(reversed(val)))+' '

    print(r.rstrip())

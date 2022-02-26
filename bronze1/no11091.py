for _ in range(int(input())):
    l = [chr(i) for i in range(97, 123)]
    s = list(input().lower())
    for val in s:
        try:
            l.remove(val)
        except:
            continue
    if l:
        print('missing '+''.join(l))
    else:
        print('pangram')
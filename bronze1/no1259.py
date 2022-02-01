while True:
    n = input()
    if n == '0':
        break
    rs = ''.join(list(reversed(n)))
    print('yes') if n == rs else print('no')
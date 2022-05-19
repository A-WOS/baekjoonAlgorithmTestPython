while 1:
    n = input()

    if n == '0':
        break

    while 1:
        n = sum(list(map(int, str(n))))

        if n // 10 == 0:
            print(n)
            break

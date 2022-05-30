while True:
    start, end = input().split()
    h1, m1 = map(int, start.split(':'))
    h2, m2 = map(int, end.split(':'))

    if h1 == m1 == h2 == m2 == 0:
        break

    t = h1 * 60 + m1 + h2 * 60 + m2
    n = t // 60 // 24
    h = str(t // 60 % 24)
    m = str(t % 60)

    if len(h) == 1:
        h = h.zfill(2)
    if len(m) == 1:
        m = m.zfill(2)

    if n > 0:
        print(f'{h}:{m} +{n}')
    else:
        print(f'{h}:{m}')

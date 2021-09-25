for _ in range(3):
    sh, sm, ss, eh, em, es = map(int, input().split())
    e_total = eh * 3600 + em * 60 + es
    s_total = sh * 60 * 60 + sm * 60 + ss
    total = e_total - s_total
    h = total // 3600
    m = (total % 3600) // 60
    s = (total % 3600) % 60
    print(h, m, s)

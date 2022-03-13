for _ in range(int(input())):
    s = list(input())
    rect = int(len(s) ** 0.5)
    secrets_l = list()
    j = 0
    rs = ''
    for i in range(rect):
        secrets_l.append(s[j:j + rect])
        j += rect

    for i in range(rect-1, -1, -1):
        for j in range(0, rect):
            rs += secrets_l[j][i]

    print(rs)

# zip()
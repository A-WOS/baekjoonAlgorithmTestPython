T = int(input())

for i in range(T):
    n = int(input())
    cvB = bin(n).replace("0b", "")

    b_list = list(map(int, cvB))
    b_list.reverse()
    count = []
    tot = 0
    for j in b_list:
        if j == 1:
            count.append(tot)
            tot += 1
        else:
            tot += 1

    c_list = map(str, count)
    print(' '.join(c_list))
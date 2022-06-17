T = int(input())
for _ in range(T):
    a = list(input())
    b = list(input())
    cnt = 0
    for _ in range(len(a)):
        if 1 == (int(a[_]) ^ int(b[_])):
            cnt += 1
    print('Hamming distance is ' + str(cnt) + ".")

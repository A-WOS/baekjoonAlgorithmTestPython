T = int(input())
for _ in range(T):
    h, m, s = map(int, input().split(':'))
    times = [str(bin(h)[2:]).zfill(6), str(bin(m)[2:]).zfill(6), str(bin(s)[2:]).zfill(6)]
    a = ''
    b = ''.join(times)
    for i in range(len(times[0])):
        for j in range(3):
            a += times[j][i]
    print(a, b)

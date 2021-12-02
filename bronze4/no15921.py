N= int(input())
if N == 0:
    print('divide by zero')
else:
    t = list(map(int, input().split()))
    r1 = sum(t) / N
    r2 =0
    for val in t:
        r2 += val*(1/N)
    print('{:.2f}'.format(r1/r2))
n_list = list(map(int, input().split()))
min_N = min(n_list)
while True:
    cnt = 0
    for i in n_list:
        if min_N % i == 0:
            cnt += 1
    if cnt >= 3:
        print(min_N)
        break
    min_N += 1

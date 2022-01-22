flag = True
n = int(input())
while flag:
    k = int(input())
    if k == 0:
        flag = False
    else:
        print(f'{k} is a multiple of {n}.') if k % n == 0 else print(f'{k} is NOT a multiple of {n}.')
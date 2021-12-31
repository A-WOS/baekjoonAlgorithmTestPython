n = int(input())
tot, i = 2, 2
count = 1
flag = True
while flag:
    for _ in range(2):
        if count == n:
            print(tot)
            flag = False
            break
        else:
            count += 1
            tot += i
    i += 1

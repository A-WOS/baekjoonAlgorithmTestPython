N = int(input())
customer = list(map(int, input().split()))
cus_list = [0 for j in range(101)]
cnt = 0
for i in customer:
    if cus_list[i] == 0:
        cus_list[i] = i
    else:
        cnt += 1
print(cnt)

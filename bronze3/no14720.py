# 딸기 0, 초코 1, 바나나 2
# milk_l = [0, 1, 2]
N = int(input())
milk_street = list(map(int, input().split()))

# print(milk_street)
# milkTotalCnt 총 3개 ,mod 3 을 하게 되면 0, 1, 2가 반복
cnt, milkTotalCnt = 0, 0
for i, val in enumerate(milk_street):
    if val == milkTotalCnt % 3:
        cnt += 1
        milkTotalCnt += 1
print(cnt)
# print(i, val)

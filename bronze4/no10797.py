no = int(input())
n = input().split()
cnt = 0
for i in n:
    if int(i) % 10 == no:
        cnt += 1
print(cnt)

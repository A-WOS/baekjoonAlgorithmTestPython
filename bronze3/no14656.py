n = int(input())
human = list(map(int, input().split()))
cnt = 0

for i in range(n):
    if human[i] != i+1:
        cnt += 1

print(cnt)

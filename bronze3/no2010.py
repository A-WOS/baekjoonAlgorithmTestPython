import sys

N = int(sys.stdin.readline().rstrip())

sum = 0
for i in range(N):
    sum += int(sys.stdin.readline().rstrip()) -1

print(sum+1)
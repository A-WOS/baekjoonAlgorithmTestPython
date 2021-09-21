import sys

N = int(sys.stdin.readline())
# 해당 크기 만큼의 배열 초기화
s1 = [['' for _ in range(N)] for _ in range(N)]
s2 = [['' for _ in range(N)] for _ in range(N)]
result = "YES"
for i in range(N):
    word = input()
    for j, val in enumerate(word, start=0):
        s1[i][j] = val
        s2[j][i] = s1[i][j]

if s1 != s2:
    result = "NO"

print(result)

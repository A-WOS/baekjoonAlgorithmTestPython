import sys

n = int(input())
file_name = []
rs = ''
for _ in range(n):
    file_name.append(list(sys.stdin.readline().rstrip()))

# 문자열의 길이
for i in range(len(file_name[0])):
    # 같은 패턴인지 찾기 위해 set() 사용
    diff_char = set()
    # 입력받은 문자열 개수
    for j in range(len(file_name)):
        diff_char.add(file_name[j][i])

    if len(diff_char) == 1:
        rs += file_name[0][i]
    else:
        rs += '?'
print(rs)

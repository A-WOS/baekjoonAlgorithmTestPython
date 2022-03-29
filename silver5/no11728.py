N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
rs = ''
for val in sorted(A + B):
    rs += f'{val} '
print(rs.rstrip())
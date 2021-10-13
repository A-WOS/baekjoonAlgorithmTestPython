# X사 1리터당 9엔
# Y사 기본요금 100엔, 20리터 이하라면 기본요금
#   1리터당 추가요금 D엔
# JOI군이 쓰는 한달간 수도의 양 P가 입력

A = int(input())
B = int(input())
C = int(input())
D = int(input())
P = int(input())

m = []

m.append(A * P)
if C >= P:
    m.append(B)
else:
    m.append(B + (P - C) * D)
print(min(m))

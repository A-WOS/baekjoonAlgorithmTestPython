import collections

T = int(input())

for _ in range(T):
    n = int(input())
    univ = []
    school, rs = '', 0
    for _ in range(n):
        u, cnt = input().split()
        univ.append([u, int(cnt)])
    for i in range(len(univ)):
        if rs < univ[i][1]:
            rs = univ[i][1]
            school = univ[i][0]
    print(school)
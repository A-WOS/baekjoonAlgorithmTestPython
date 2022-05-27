T = int(input())
for _ in range(T):
    s = int(input())
    n = int(input())
    rs = s

    for _ in range(n):
        q, p = map(int, input().split())
        rs += q * p

    print(rs)
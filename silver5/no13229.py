n = int(input())
n_l = list(map(int, input().split()))
for _ in range(int(input())):
    a, b = map(int, input().split())
    print(sum(n_l[a:b+1]))

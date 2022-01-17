t = int(input())
for _ in range(t):
    l = list(map(int, input().split()))
    k = list()
    for val in l:
        if val % 2 == 0:
            k.append(val)
    print(sum(k), min(k))
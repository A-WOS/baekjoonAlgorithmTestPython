N = int(input())
l = sorted(map(int, input().split()))
if N % 2 == 1:
    if N == 1:
        print(l[0]**2)
    else:
        print(l[int(len(l) / 2)]**2)
else:
    print(min(l)*max(l))
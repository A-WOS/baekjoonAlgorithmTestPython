T = int(input())
a, b = 0, 0
for _ in range(T):
    A, B = map(int, input().split())
    if A > B:
        a += 1
    elif B > A:
        b += 1

print(a, b)

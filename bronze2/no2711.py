T = int(input())
for _ in range(T):
    i, s = input().split()
    s = list(s)
    s.pop(int(i)-1)
    print(''.join(s))
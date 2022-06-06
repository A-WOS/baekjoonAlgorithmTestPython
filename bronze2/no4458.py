import sys

N = int(input())
for _ in range(N):
    s = list(sys.stdin.readline().rstrip())
    s[0] = s[0].upper()
    print(''.join(s))
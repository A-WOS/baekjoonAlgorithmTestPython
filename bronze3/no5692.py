import sys
from math import factorial

while True:
    n = sys.stdin.readline().rstrip()
    if n == '0':
        break

    tot, cnt = 0, 0
    for i in range(len(n), 0, -1):
        tot += int(n[cnt]) * factorial(int(i))
        cnt += 1
    print(tot)

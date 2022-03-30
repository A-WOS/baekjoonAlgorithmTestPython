import sys

N = int(input())
numbers = []
for _ in range(N):
    numbers.append(int(sys.stdin.readline().rstrip()))
print('\n'.join(map(str, sorted(numbers))))
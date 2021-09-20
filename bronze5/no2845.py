import sys
x, y = map(int, sys.stdin.readline().split())
result = []
for val in list(map(int, sys.stdin.readline().split())):
    result.append(val - x * y)
print(" ".join(map(str, result)))

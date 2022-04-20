from math import factorial


t = int(input())
for _ in range(t):
    n = int(input())
    print(str(factorial(n)).rstrip('0')[-1])
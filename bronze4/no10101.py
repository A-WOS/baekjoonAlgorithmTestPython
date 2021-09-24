import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

result = "Error"
angle_sum = a+b+c
if a == b == c:
    result = "Equilateral"
elif angle_sum == 180 and a == b != c or a == c != b or b == c != a:
    result = "Isosceles"
elif angle_sum == 180 and a != b != c:
    result = "Scalene"

print(result)
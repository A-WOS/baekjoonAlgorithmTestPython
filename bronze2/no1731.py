numbers = []
n = int(input())
for _ in range(n):
    numbers.append(int(input()))

rs = numbers[-1]
if numbers[2] - numbers[1] == numbers[1] - numbers[0]:
    rs += (numbers[1] - numbers[0])
else:
    rs *= (numbers[1] // numbers[0])
print(rs)
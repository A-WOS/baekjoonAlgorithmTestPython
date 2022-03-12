numbers_len = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
for i in range(len(numbers)):
    numbers[i] = str(numbers[i])
print(' '.join(numbers))
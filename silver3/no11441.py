import sys


def prefix_sum(nums):
    rs = 0
    for num in nums:
        rs += num
        yield rs


N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
sum_numbers = list(prefix_sum(numbers))

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    i, j = map(int, sys.stdin.readline().split())

    if i == j:
        print(numbers[i-1])
    elif i > 1:
        print(sum_numbers[j-1] - sum_numbers[i-2])
    else:
        print(sum_numbers[j-1])

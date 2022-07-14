nums = [1] * 117
n = int(input())
for i in range(4, n + 1):
    nums[i] = nums[i - 3] + nums[i - 1]
print(nums[n])

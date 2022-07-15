n = int(input())
nums = [0] * (n + 2)
nums[1] = 1
for i in range(2, n + 2):
    nums[i] = nums[i - 1] + nums[i - 2]

print((nums[n] + nums[n + 1]) * 2)

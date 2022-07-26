import sys

n, q = map(int, input().split())
nums = list(map(int, sys.stdin.readline().split()))
for _ in range(q):
    l = list(map(int, sys.stdin.readline().split()))
    if l[0] == 1:
        print(sum(nums[l[1]-1:l[2]]))
        tmp = nums[l[1]-1]
        nums[l[1]-1] = nums[l[2]-1]
        nums[l[2]-1] = tmp
    else:
        print(sum(nums[l[1] - 1:l[2]]) - sum(nums[l[3] - 1:l[4]]))


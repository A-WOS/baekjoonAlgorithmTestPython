import sys

teams = int(input())
ability = sorted(map(int, sys.stdin.readline().split()))
left, right = 0, teams*2 - 1
rs = 199999
while left < right:
    if ability[left] + ability[right] < rs:
        rs = ability[left] + ability[right]
    left += 1
    right -= 1
print(rs)

# false
# students = set(map(int, sys.stdin.readline().split()))
# # rs = set()
# rs = 0
# # for _ in range(teams):
# for i in range(teams - 1):
#     # rs.add(max(students)+min(students))
#     # rs = max(students)+min(students)
#     max(students[i]) + min(students[i])
#     students.remove(max(students))
#     students.remove(min(students))
#
# print(min(rs))

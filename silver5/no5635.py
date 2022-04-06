
# solved dict
# import collections
#
#
# def change_str(param):
#     if len(param) == 1:
#         param = '0' + param
#     return param
#
#
# n = int(input())
# students = collections.defaultdict(str)
# for _ in range(n):
#     name, day, mon, year = input().split()
#     students[int(year+change_str(mon)+change_str(day))] = name
#
# print(max(students.items())[1])
# print(min(students.items())[1])


# solved list
def change_str(param):
    if len(param) == 1:
        param = '0' + param
    return param


n = int(input())
students = []
for _ in range(n):
    name, day, mon, year = input().split()
    students.append([int(year + change_str(mon) + change_str(day)), name])
print(max(sorted(students))[1])
print(min(sorted(students))[1])

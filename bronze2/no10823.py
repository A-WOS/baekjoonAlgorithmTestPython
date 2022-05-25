import sys

rs = 0
nums = sys.stdin.read().split(',')
for num in nums:
    rs += int(num.replace('\n', ''))
print(rs)
# while True:
#     try:
#
#         for num in nums:
#             if num:
#                 rs += int(num)
#                 print(rs)
#     except EOFError:
#         break

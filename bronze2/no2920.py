# solved #2
num_l = input().split()
a = ''
for val in num_l: a += val
print('ascending') if a == '12345678' else print('descending') if a == '87654321' else print('mixed')

# solved #1
# a = [1, 2, 3, 4, 5, 6, 7, 8]
# d = [8, 7, 6, 5, 4, 3, 2, 1]
# if num_l == a:
#     print('ascending')
# elif num_l == d:
#     print('descending')
# else:
#     print('mixed')

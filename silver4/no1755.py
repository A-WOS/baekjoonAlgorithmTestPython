import collections

numbers = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three',
           '4': 'four', '5': 'five', '6': 'six', '7': 'seven',
           '8': 'eight', '9': 'nine'}

M, N = map(int, input().split())
print(sorted(numbers.values()))
rs_numbers = []
for i in range(M, N + 1):
    rs = ''
    # rs.append(numbers[val] for val in list(str(i))))
    for val in list(str(i)):
        rs += f'{numbers[val]} '
    rs_numbers.append(rs.rstrip())
print(rs_numbers)
    # print(next(numbers[val] for val in list(str(i))))
    # print(numbers['0'])
    # for val in list(str(i)):
    #     ''.join(numbers)

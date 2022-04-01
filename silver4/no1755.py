import collections

org_numbers = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three',
           '4': 'four', '5': 'five', '6': 'six', '7': 'seven',
           '8': 'eight', '9': 'nine'}

new_numbers = collections.defaultdict(str)
zip_numbers = collections.defaultdict(str)
M, N = map(int, input().split())
for number in range(M, N+1):
    rs = ''
    for val in str(number):
        rs += f'{org_numbers[val]} '
    new_numbers[str(number)] = rs.strip()

zip_numbers = dict(zip(new_numbers.values(), new_numbers.keys()))
count = 0
for val in sorted(new_numbers.values()):
    count += 1
    print(zip_numbers[val], end=' ')
    if count % 10 == 0:
        print()

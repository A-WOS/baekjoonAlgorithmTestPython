def convert_size(n1, n2):
    temp = numbers[n1]
    numbers[n1] = numbers[n2]
    numbers[n2] = temp
    return


numbers = dict()
n = list(map(int, input().split()))
s = input()
for i, ch in enumerate(s):
    numbers[ch] = n[i]

for num in numbers:
    if numbers['A'] > numbers['B']:
        convert_size('A', 'B')
    elif numbers['B'] > numbers['C']:
        convert_size('B', 'C')
    elif numbers['A'] > numbers['C']:
        convert_size('A', 'C')

print(' '.join(map(str, list(numbers.values()))))

numbers = []
for _ in range(4):
    numbers.append(int(input()))

cnt = 0
for i in range(3):
    if numbers[i] < numbers[i + 1]:
        cnt += 1
    if numbers[i] > numbers[i+1]:
        cnt -= 1

if len(set(numbers)) == 1:
    print('Fish At Constant Depth')
elif cnt == 3:
    print('Fish Rising')
elif cnt == -3:
    print('Fish Diving')
else:
    print('No Fish')

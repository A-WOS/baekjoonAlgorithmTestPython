from collections import Counter

numbers = []
while True:
    try:
        numbers.append(int(input()))
    except EOFError:
        break
avg = sum(numbers) // len(numbers)
c = Counter(numbers).most_common(1)[0][0]
print(avg)
print(c)
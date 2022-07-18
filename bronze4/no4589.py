T = int(input())
print('Gnomes:')
for _ in range(T):
    numbers = list(map(int, input().split()))
    print('Ordered') if numbers == sorted(numbers) or numbers == sorted(numbers, reverse=True) else print('Unordered')


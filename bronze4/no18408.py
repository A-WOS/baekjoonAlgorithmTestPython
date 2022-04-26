numbers = list(map(int, input().split()))
print(1 if numbers.count(1) > numbers.count(2) else 2)
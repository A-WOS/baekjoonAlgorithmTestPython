N = int(input())
numbers = [2 ** n for n in range(31)]
print(1) if N in numbers else print(0)

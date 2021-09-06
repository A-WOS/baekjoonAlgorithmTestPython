s = input().split()
result = []
for val in s:
    result.append(int(val[::-1]))
print(int(str(sum(result))[::-1]))
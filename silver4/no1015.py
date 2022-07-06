N = int(input())
numbers = list(map(int, input().split()))
sort_numbers = sorted(numbers)
rs = []
for i in range(N):
    idx = sort_numbers.index(numbers[i])
    rs.append(idx)
    # print(f'rs: {rs}')
    # print(f'idx: {idx}', f'numbers: {numbers[i]}')
    sort_numbers[idx] = -1
    # print(f'sort_numbers: {sort_numbers}')
print(*rs)

from itertools import combinations

human = [int(input()) for _ in range(9)]

rs = 0
for val in combinations(human, 7):
    if sum(val) == 100:
        rs = sorted(val)
        for num in sorted(val):
            print(num)
        break

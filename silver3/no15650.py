import re
from itertools import combinations

N, M = map(int, input().split())
numbers = list(range(1, N + 1))
for key in combinations(numbers, M):
    print(re.sub(r'[^0-9\s]', '', str(key)))
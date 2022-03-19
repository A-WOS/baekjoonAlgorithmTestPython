import re
from itertools import product

N, M = map(int, input().split())
numbers = sorted(str(val) for val in range(1, N + 1))
for key in product(numbers, repeat=M):
    print(re.sub(r'[^0-9\s]', '', str(key)))
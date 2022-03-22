import re
from itertools import product

N, M = map(int, input().split())
numbers = sorted(map(int, input().split()))
for key in product(numbers, repeat=M):
    print(re.sub(r'[^0-9\s]', '', str(key)))
import re
from itertools import combinations_with_replacement

N, M = map(int, input().split())
numbers = sorted(map(int, input().split()))
for key in combinations_with_replacement(numbers, M):
    print(re.sub(r'[^0-9\s]', '', str(key)))
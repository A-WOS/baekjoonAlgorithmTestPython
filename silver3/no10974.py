import re
from itertools import permutations

N = int(input())

for val in permutations(list(range(1, N+1)),N):
    print(re.sub(r'[^0-9\s]', '', str(val)))
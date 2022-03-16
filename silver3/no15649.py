import re
from itertools import permutations

N, M = map(int, input().split())
numbers = list(range(1, N + 1))
if M == 1:
    for val in numbers:
        print(val)
else:
    for key in permutations(numbers, M):
        print(re.sub(r'[^0-9\s]', '', str(key)))

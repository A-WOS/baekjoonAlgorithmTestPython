import re
import sys
from itertools import permutations

N, M = map(int, input().split())
numbers = sorted(map(int, sys.stdin.readline().rstrip().split()))
for key in permutations(numbers, M):
    print(re.sub(r'[^0-9\s]', '', str(key)))

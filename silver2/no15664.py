import re
from itertools import combinations

N, M = map(int, input().split())
numbers = sorted(map(int, input().split()))
rs = []
for key in combinations(numbers, M):
    rs.append(key)

for val in sorted(set(rs)):
    print(re.sub(r'[^0-9\s]', '', str(val)))
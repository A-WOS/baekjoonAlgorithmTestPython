import re
from itertools import combinations_with_replacement

N, M = map(int, input().split())
numbers = sorted(map(int, input().split()))
rs = []
for key in combinations_with_replacement(numbers, M):
    rs.append(key)

for val in sorted(set(rs)):
    print(re.sub(r'[^0-9\s]', '', str(val)))

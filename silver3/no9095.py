import re
from itertools import product

number = [1, 2, 3]
for _ in range(int(input())):
    N = int(input())

    rs = []
    for i in range(N, 0, -1):
        for val in product(number, repeat=i):
            if sum(map(int, re.sub(r'[^0-9\s]', '', str(val)).split())) == N:
                rs.append(re.sub(r'[^0-9\s]', '', str(val)))
    print(len(rs))

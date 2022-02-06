from itertools import permutations

n = int(input())
k = int(input())
card_l = list(input() for _ in range(n))
rs = set()
for val in permutations(card_l, k):
    # print(''.join(val))
    rs.add(''.join(val))
print(len(rs))
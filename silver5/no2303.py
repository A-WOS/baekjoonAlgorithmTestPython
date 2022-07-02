from itertools import combinations

N = int(input())
rs_score, rs = 0, 0
for i in range(1, N + 1):
    humans = list(map(int, input().split()))
    scores = set()
    for score in combinations(humans, 3):
        scores.add(int(str(sum(score))[-1]))
    if rs_score <= max(scores):
        rs_score, rs = max(scores), i
print(rs)

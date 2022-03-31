import collections
import sys

N, rp = map(int, input().split())
pocket_mons = collections.defaultdict(str)
for i in range(N):
    pocket_mons[i + 1] = sys.stdin.readline().rstrip()

switch_pocket_mons = dict(zip(pocket_mons.values(), pocket_mons.keys()))
for _ in range(rp):
    rs = sys.stdin.readline().rstrip()
    try:
        if int(rs):
            print(pocket_mons[int(rs)])
    except ValueError:
        print(switch_pocket_mons[rs])

N, M = map(int, input().split())
if 1 <= M <= 2:
    print("NEWBIE!")
elif N >= M != 1 and M !=2:
    print("OLDBIE!")
elif N < M:
    print("TLE!")
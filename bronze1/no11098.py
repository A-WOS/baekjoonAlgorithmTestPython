n = int(input())
for _ in range(n):
    p = int(input())
    players = dict()
    for _ in range(p):
        c, name = input().split()
        players[int(c)] = name
    print(players[max(players.keys())])
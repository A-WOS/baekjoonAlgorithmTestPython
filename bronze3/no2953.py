r = [sum(map(int, input().split())) for _ in range(5)]
print(r.index(max(r))+1, max(r))

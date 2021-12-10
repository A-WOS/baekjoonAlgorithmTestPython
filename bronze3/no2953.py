r = []
for _ in range(5):
    r.append(sum(list(map(int, input().split()))))
print(r.index(max(r))+1, max(r))

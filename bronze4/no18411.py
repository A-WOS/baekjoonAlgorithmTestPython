score = sorted(map(int, input().split()), reverse=True)
print(sum(score[:2]))
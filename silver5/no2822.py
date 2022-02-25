score = list()
for _ in range(8):
    score.append(int(input()))

score_dict = dict()
for i, v in enumerate(score):
    score_dict[i+1] = v

rs = list()
tot = 0
for val in sorted(score_dict.items(), key=lambda x: x[1], reverse=True)[:5]:
    rs.append(str(list(val)[0]))
    tot += list(val)[1]
print(tot)
print(' '.join(sorted(rs)))

l = [i for i in range(1, int(input())+1)]
result = []
cnt = 1
while l:
    if cnt % 2 == 0:
        l.append(l[0])
        l.pop(0)
    else:
        result.append(l[0])
        l.pop(0)
    cnt += 1

print(' '.join(map(str, result)))
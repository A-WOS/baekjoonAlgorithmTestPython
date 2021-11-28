w, k = [], []
for i in range(20):
    if i < 10:
        w.append(int(input()))
    else:
        k.append(int(input()))

w = sorted(w)
k = sorted(k)
print(sum(w[-3:]), sum(k[-3:]))
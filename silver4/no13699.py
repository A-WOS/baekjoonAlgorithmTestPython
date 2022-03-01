n = int(input())
t = [1]
for val in range(1, 36):
    j = val - 1
    tot = 0
    for i in range(val):
        tot += (t[i] * t[j])
        j -= 1
    t.append(tot)

print(t[n])

N = int(input())
h = []
max = -1
count = 0
for i in range(N):
    h.append(int(input()))
    if max < h[i]:
        max = h[i]
        count += 1

print(count)

max = -1
count = 0
h.reverse()
for i in h:
    if max < i:
        max = i
        count +=1
print(count)
N = int(input())
name = []
for _ in range(N):
    name.append(input())
if name == sorted(name, reverse=True):
    print('DECREASING')
elif name == sorted(name):
    print('INCREASING')
else:
    print('NEITHER')
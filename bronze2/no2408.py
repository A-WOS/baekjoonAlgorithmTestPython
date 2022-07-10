N = int(input())*2-1
s = ''
for _ in range(N):
    s += input()
print(eval(s.replace('/', '//')))


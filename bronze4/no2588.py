a = input()
b = input()
for i in reversed(range(len(a))):
    print(int(a) * int(b[i]))
print(int(a) * int(b))
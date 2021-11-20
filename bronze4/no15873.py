x = input()
if x[1] == '0':
    print(10 + int(x[2:]))
else:
    print(int(x[0]) + int(x[1:]))
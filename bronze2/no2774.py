T = int(input())

for _ in range(T):
    x = input()
    numbers = []

    rs = 0
    for i in range(len(x)):
        if int(x[i]) not in numbers:
            rs += 1
            numbers.append(int(x[i]))

    print(rs)

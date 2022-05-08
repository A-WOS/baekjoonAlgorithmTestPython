# print(type(ord('A')))
T = int(input())

for _ in range(T):
    alphas, numbers = input().split('-')
    numbers = int(numbers)

    tot = 0
    for j in range(len(alphas)):
        tot += (ord(alphas[j]) - 65) * 26 ** (2 - j)

    print('nice') if abs(tot-numbers) <= 100 else print('not nice')

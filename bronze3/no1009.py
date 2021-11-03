T = int(input())

two = [2, 4, 8, 6]
three = [3, 9, 7, 1]
four = [4, 6]
seven = [7, 9, 3, 1]
eight = [8, 4, 2, 6]
nine = [9, 1]

for i in range(T):
    a, b = map(int, input().split())
    a %= 10
    if a == 0:
        print(10)
    elif a == 1:
        print(1)
    elif a == 2:
        print(two[(b % len(two)) - 1])
    elif a == 3:
        print(three[(b % len(three)) - 1])
    elif a == 4:
        print(four[(b % len(four)) - 1])
    elif a == 5:
        print(5)
    elif a == 6:
        print(6)
    elif a == 7:
        print(seven[(b % len(seven)) - 1])
    elif a == 8:
        print(eight[(b % len(eight)) - 1])
    elif a == 9:
        print(nine[(b % len(nine)) - 1])
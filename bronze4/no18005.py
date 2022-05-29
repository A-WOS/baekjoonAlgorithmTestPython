n = int(input())
if n % 2 == 0:
    if (n // 2) % 2 == 1:
        print(1)
    else:
        print(2)
else:
    print(0)

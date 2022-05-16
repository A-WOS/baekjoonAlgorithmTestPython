for _ in range(int(input())):
    numbers = list(map(int, input().split()))[1:]
    odd = even = 0
    for n in numbers:
        if n % 2 == 1:
            odd += n
        else:
            even += n
    if odd == even:
        print("TIE")
    elif odd > even:
        print("ODD")
    else:
        print("EVEN")

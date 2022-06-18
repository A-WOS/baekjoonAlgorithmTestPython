for _ in range(int(input())):
    n = input()
    numbers = str(int(n) + int(n[::-1]))
    print("YES" if numbers == numbers[::-1] else "NO")
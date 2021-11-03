while True:
    try:
        s = input()
    except EOFError:
        break
    print(s)
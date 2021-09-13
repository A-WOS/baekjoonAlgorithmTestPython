N = input()
F = input()

r = int(N) - int(N[-2:])
while True:
    if r % int(F) == 0:
        str_r = str(r)
        print(str_r[-2:])
        break

    r += 1

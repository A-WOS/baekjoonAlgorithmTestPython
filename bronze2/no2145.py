def repeat_sum(n):
    tot = 0
    if len(n) == 1:
        return n
    else:
        for val in n:
            tot += int(val)
        return repeat_sum(str(tot))


while True:
    n = input()
    if n == '0':
        break
    else:
        print(repeat_sum(n))

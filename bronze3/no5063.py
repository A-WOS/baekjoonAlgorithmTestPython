for _ in range(int(input())):
    r, e, c = map(int, input().split())
    k = e - c
    if r == k:
        print('does not matter')
    elif r > k:
        print('do not advertise')
    else:
        print('advertise')
    # if r < 0 and k < 0:
    #     print('do not advertise')
    # elif r > k:
    #     print('does not matter')
    # else:

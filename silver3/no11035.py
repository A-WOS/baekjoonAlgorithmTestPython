while True:
    try:
        N, K = map(int, input().split())
        numbers = [num for num in range(2, N + 1)]
        cnt = 0
        i = 2
        flag = True

        while numbers:
            for number in numbers:
                if number % i == 0:
                    cnt += 1
                    if cnt == K:
                        flag = False
                        print(number)
                        break
                    else:
                        numbers.remove(number)
            if not flag:
                break
            i += 1
    except EOFError:
        break

for _ in range(int(input())):
    x = int(input())
    n = x//2
    l = []
    for i in range(x-1, n, -1):
        if x - i == i:
            continue
        else:
            l.append(f'{x - i} {i}')
    print(f'Pairs for {x}: ' + ', '.join(val for val in l).strip())
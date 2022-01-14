for _ in range(int(input())):
    x = int(input())
    n = x//2
    l = []
    for i in range(1, n+1):
        if i < x - i: l.append(f'{i} {x - i}')
    print(f'Pairs for {x}: ' + ', '.join(val for val in l))
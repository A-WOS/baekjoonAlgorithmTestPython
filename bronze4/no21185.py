n = int(input())
res1 = sum(x for x in range(1, n+1)) % 2
res2 = sum(y for y in range(n, 101)) % 2
print('Odd') if res1 == 1 and res2 == 1 else print('Even') if res1 == 0 and res2 == 0 else print('Either')
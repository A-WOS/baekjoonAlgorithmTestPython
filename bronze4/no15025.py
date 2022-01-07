n, m = map(int, input().split())
print('Not a moose') if n == m == 0 else print(f'Even {n+m}') if n == m != 0 else print(f'Odd {max(n,m)*2}')
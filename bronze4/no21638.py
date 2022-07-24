t1, w1 = map(int, input().split())
t2, w2 = map(int, input().split())
if t2 < 0 and w2 >= 10:
    print('A storm warning for tomorrow! Be careful and stay home if possible!')
elif t2-t1 < 0:
    print('MCHS warns! Low temperature is expected tomorrow.')
elif w2-w1 > 0:
    print('MCHS warns! Strong wind is expected tomorrow.')
else:
    print('No message')
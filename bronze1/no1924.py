m, d = map(int, input().split())

tot = 0
cals = {1: 31, 2: 28, 3: 31, 4: 30,
        5: 31, 6: 30, 7: 31, 8: 31,
        9: 30, 10: 31, 11: 30, 12: 31}

for i in range(1, m):
    tot += cals[i]
tot += d
rs = tot % 7

if rs == 0:
    print('SUN')
elif rs == 1:
    print('MON')
elif rs == 2:
    print('TUE')
elif rs == 3:
    print('WED')
elif rs == 4:
    print('THU')
elif rs == 5:
    print('FRI')
elif rs == 6:
    print('SAT')


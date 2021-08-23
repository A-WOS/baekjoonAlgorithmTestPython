s_dict = {'1': 'A', '2': 'B', '3': 'C', '0': 'D', '4': 'E'}

for i in range(3):
    s = input().split()

    if s.count('0') == 4:
        print(s_dict['0'])
    elif s.count('0') == 1:
        print(s_dict['1'])
    elif s.count('0') == 2:
        print(s_dict['2'])
    elif s.count('0') == 3:
        print(s_dict['3'])
    elif s.count('1') == 4:
        print(s_dict['4'])

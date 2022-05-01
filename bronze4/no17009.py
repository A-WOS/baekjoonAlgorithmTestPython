a_rs = sum([int(input())*i for i in range(3, 0, -1)])
b_rs = sum([int(input())*i for i in range(3, 0, -1)])
print('A') if a_rs > b_rs else print('B') if a_rs < b_rs else print('T')
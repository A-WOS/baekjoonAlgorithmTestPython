s_N = bin(int(input())).replace("0b", "")
arr_list = '0b'+''.join(list(reversed(s_N)))
print(int(arr_list, 2))
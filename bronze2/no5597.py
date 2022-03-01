std_list = list(str(val) for val in range(1, 31))
for i in range(28): std_list.remove(input())
for val in std_list: print(val)
temp_list = []
tot_list = []
while True:
    a = float(input())
    if a == 999:
        break
    temp_list.append(a)

for i in range(len(temp_list)):
    if i > 0 :
        print("{:.2f}".format(temp_list[i] - temp_list[i-1]))

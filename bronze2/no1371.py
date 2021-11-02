dict_c = {'0': 'a', '1': 'b', '2': 'c', '3': 'd', '4': 'e', '5': 'f', '6': 'g', '7': 'h', '8': 'i', '9': 'j', '10': 'k',
          '11': 'l', '12': 'm', '13': 'n', '14': 'o', '15': 'p', '16': 'q', '17': 'r', '18': 's', '19': 't', '20': 'u',
          '21': 'v',
          '22': 'w', '23': 'x', '24': 'y', '25': 'z'}
list_s = ''
many_s = []
rs = ''
while True:
    try:
        s = input()
    except EOFError:
        break
    else:
        list_s += s

for i in dict_c:
    many_s.append(list_s.count(dict_c.get(i)))

for i in range(len(many_s)):
    if max(many_s) == list_s.count(dict_c.get(str(i))):
        rs += dict_c.get(str(i))
    else:
        continue
print(rs)

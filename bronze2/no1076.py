dict_s = {"black": "0",
          "brown": "1",
          "red": "2",
          "orange": "3",
          "yellow": "4",
          "green": "5",
          "blue": "6",
          "violet": "7",
          "grey": "8",
          "white": "9",
          }
r = ""
for x in range(3):
    s = input()
    if x == 2:
        converter = str(10 ** int(dict_s.get(s)))
        r += converter[1:]

    else:
        r += (dict_s.get(s))
print(int(r))

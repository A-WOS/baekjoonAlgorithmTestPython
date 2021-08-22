s_list = []
while True:
    s = input()
    if s == "#":
        break
    else:
        c_dict = {"-": 0, "\\": 1, "(": 2, "@": 3, "?": 4, ">": 5, "&": 6, "%": 7, "/": -1}
        len_s = len(s)

        sum = 0
        for i in range(len_s):
            sum += c_dict[s[i]] * (8 ** (len_s - i - 1))

    print(sum)

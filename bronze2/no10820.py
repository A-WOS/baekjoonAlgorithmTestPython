# upper_case = [chr(val) for val in range(65, 91)]
# lower_case = [chr(val) for val in range(97, 123)]
# space_case = chr(32)
# number_case = [chr(val) for val in range(48, 58)]
while True:
    try:
        low, up, num, sp = 0, 0, 0, 0
        s = list(input())
        for val in s:
            if 97 <= ord(val) <= 122:
                low += 1
            elif 65 <= ord(val) <= 90:
                up += 1
            elif 48 <= ord(val) <= 57:
                num += 1
            elif ord(val) == 32:
                sp += 1
        print(low, up, num, sp)
    except EOFError:
        break




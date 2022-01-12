def man(*args):
    if b_m == s_m:
        if b_d <= s_d:
            return s_y - b_y
        else:
            return s_y - b_y - 1
    elif b_m < s_m:
        return s_y - b_y
    else:
        return s_y - b_y - 1


b_y, b_m, b_d = map(int, input().split())
s_y, s_m, s_d = map(int, input().split())

print(man(b_y, b_m, b_d, s_y, s_m, s_d))
print(1 + s_y - b_y)
print(s_y - b_y)

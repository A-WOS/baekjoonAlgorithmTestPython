# 932
# 9x3 = 27
# 2x2
# 4*1
# 4

def repeat(f, l):
    result = str(int(f)*int(l))
    if len(result) == 1:
        return 'FA'
    f = result[0]
    l = len(result)
    return repeat(f, l)


x = input()
f = x[0]
l = len(x)

print(repeat(f, l))


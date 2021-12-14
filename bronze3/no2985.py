def result(a, opt1, b, opt2, c):
    return str(a) + opt1 + str(b) + opt2 + str(c)


a, b, c = map(int, input().split())
if a < b and c < b:
    if a == b + c:
        print(result(a, '=', b, '+', c))
    elif a == b - c:
        print(result(a, '=', b, '-', c))
    elif a == b / c:
        print(result(a, '=', b, '/', c))
    elif a == b * c:
        print(result(a, '=', b, '*', c))
else:
    if c == a + b:
        print(result(a, '+', b, '=', c))
    elif c == a - b:
        print(result(a, '-', b, '=', c))
    elif c == a / b:
        print(result(a, '/', b, '=', c))
    elif c == a * b:
        print(result(a, '*', b, '=', c))

def same_len(a, b):
    rs = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            rs += 1
    return rs


def diff_len(a, b):
    c = len(b) - len(a) + 1
    rs = list()

    for i in range(c):
        tot = 0
        for j, val in enumerate(b[i:i+len(a)]):
            if val != a[j]:
                tot += 1
        rs.append(tot)
    return min(rs)


a, b = input().split()
if len(a) == len(b):
    print(same_len(a, b))
else:
    print(diff_len(a, b))


# 반례
# azc xyabcxy
# 정답 1 오답 3

# not solved
# def same_len(a, b):
#     rs = 0
#     for i in range(len(a)):
#         if a[i] != b[i]:
#             rs += 1
#     return rs
#
#
# def diff_len(a, b):
#     c = len(b) - len(a)
#     w1 = b[:c] + a
#     w2 = a + b[-c:]
#     return w1, w2
#
#
# a, b = input().split()
# if len(a) == len(b):
#     print(same_len(a, b))
# else:
#     if b.count(a):
#         print(0)
#     else:
#         s1, s2 = diff_len(a, b)
#         print(min(same_len(s1, b), same_len(s2, b)))

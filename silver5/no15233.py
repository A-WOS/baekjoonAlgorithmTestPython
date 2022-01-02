def p_count(p_l):
    cnt = 0
    for val in p_l:
        cnt += g_p.count(val)
    return cnt


a,b,p = map(int, input().split())
a_p = input().split()
b_p = input().split()
g_p = input().split()
a_count, b_count = p_count(a_p), p_count(b_p)
print('TIE') if a_count == b_count else print('A') if a_count > b_count else print('B')
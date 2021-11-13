from decimal import Decimal

T = int(input())
q, d, n, p = Decimal('0.25'), Decimal('0.10'), Decimal('0.05'), Decimal('0.01')
for i in range(T):
    x = Decimal(input()) * Decimal('0.01')
    q_c = x // q
    x %= q
    d_c = x // d
    x %= d
    n_c = x // n
    x %= n
    p_c = x // p
    x %= p
    print(int(q_c), int(d_c), int(n_c), int(p_c))
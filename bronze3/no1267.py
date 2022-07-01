N = int(input())
fees = list(map(int, input().split()))
y, m = 0, 0
for fee in fees:
    y += (fee // 30 + 1) * 10
    m += (fee // 60 + 1) * 15
print(f'Y {y}') if y < m else print(f'M {m}') if y > m else print(f'Y M {y}')

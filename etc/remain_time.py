r1, r2 = 0, 0
for _ in range(8):
    a, b = map(int, input().split())
    r1 += a
    r2 += b
r_h = r1 // 60
r_m = r1 % 60 + r2 // 60
if r_m > 60:
    r_h += 1
    r_m -= 60
r_s = r2 % 60
print(f'남은시간은 {r_h}시간 {r_m}분 {r_s}초 입니다.')



s_h, s_m, s_s = map(int, input().split(' : '))
e_h, e_m, e_s = map(int, input().split(' : '))
rs1 = s_h * 3600 + s_m * 60 + s_s
rs2 = e_h * 3600 + e_m * 60 + e_s
print(rs2 - rs1 + 3600 * 24 if rs1 > rs2 else rs2 - rs1)

a = int(input())
x = int(input())
b = int(input())
y = int(input())
t = int(input())
rs1 = a + max(t - 30, 0) * x * 21
rs2 = b + max(t - 45, 0) * y * 21
print(rs1, rs2)

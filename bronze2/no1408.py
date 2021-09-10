n1, n2, n3 = map(int, input().split(":"))
m1, m2, m3 = map(int, input().split(":"))
t = m1 * 60 * 60 + m2 * 60 + m3 - (n1 * 60 * 60 + n2 * 60 + n3)

if t < 0:
    t += 60 * 60 * 24
r1 = t // 3600
r2 = (t % 3600) // 60
r3 = t % 60
print("%02d:%02d:%02d" % (r1, r2, r3))

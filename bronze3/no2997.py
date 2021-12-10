n = sorted(list(map(int,input().split())))
r_diff = min(abs(n[0]-n[1]), abs(n[1]-n[2]), abs(n[0]-n[2]))
print(n[0] + r_diff if n[0] + r_diff != n[1] else n[1] + r_diff if n[1] + r_diff != n[2] else n[2] + r_diff)
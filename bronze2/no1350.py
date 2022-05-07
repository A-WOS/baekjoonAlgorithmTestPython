files_count = int(input())
files = list(map(int, input().split()))
cluster = int(input())

tot = 0
for file in files:
    rs = file // cluster
    if file == 0:
        continue
    elif rs != 0:
        tot += rs
        if file % cluster:
            tot += 1
    else:
        tot += 1

print(tot * cluster)
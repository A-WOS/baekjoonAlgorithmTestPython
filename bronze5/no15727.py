n = int(input())
count = 0
if n < 6 :
    count = 1
else:
    count = n // 5
    if n % 5 != 0:
        count += 1

print(count)

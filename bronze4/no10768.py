m = int(input())
d = int(input())
if m*31+d == 80:
    print("Special")
elif m*31+d > 80:
    print("After")
else:
    print("Before")

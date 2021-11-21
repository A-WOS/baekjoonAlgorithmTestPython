s, k, h = map(int, input().split())
result = [s, k, h]
if sum(result) >= 100:
    print("OK")
else:
    if min(result) == s:
        print("Soongsil")
    elif min(result) == k:
        print("Korea")
    else:
        print("Hanyang")

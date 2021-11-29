T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    count = 0
    for i in range(n, m+1):
        str(i)
        count += str(i).count('0')
    print(count)
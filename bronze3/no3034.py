N, W, H = map(int, input().split())
length = (W**2 + H**2)**(1/2)
for _ in range(N):
    s = int(input())
    print('DA' if s <= length else 'NE')
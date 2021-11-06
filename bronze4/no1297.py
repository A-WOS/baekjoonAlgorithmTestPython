D, H, W = map(int, input().split())
rate = (D**2 / (H**2 + W**2))**0.5
print(int(rate*H), int(rate*W))

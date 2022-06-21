N, K = map(int, input().split())
gugu = [int(str(N*k)[::-1]) for k in range(1, K+1)]
print(max(gugu))
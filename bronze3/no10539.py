count_B = int(input())
B = list(map(int, input().split()))
A = [B[0]]
for i in range(1, count_B):
    A.append(B[i] * (i + 1) - sum(A))

print(' '.join(map(str, A)))

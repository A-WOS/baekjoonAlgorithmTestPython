S = list(input())
T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    S[A], S[B] = S[B], S[A]

print(''.join(S))

# 일반적인 변수값 바꾸기
# tmp = S[A]
# S[A] = S[B]
# S[B] = tmp

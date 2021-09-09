M = int(input())
N = int(input())
sqrt_list = []
for i in range(M, N+1):
    T = int(i ** 0.5) ** 2
    if i == T:
        sqrt_list.append(i)

if sqrt_list:
    print(sum(sqrt_list))
    print(min(sqrt_list))
else:
    print(-1)

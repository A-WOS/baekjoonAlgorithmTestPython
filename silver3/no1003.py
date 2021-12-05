zero = [1, 0, 1]
one = [0, 1, 1]

T = int(input())
for _ in range(T):
    N = int(input())
    if len(zero) <= N:
        for i in range(len(zero), N + 1):
            zero.append(zero[i - 1] + zero[i - 2])
            one.append(one[i - 1] + one[i - 2])
    print(f"{zero[N]}", f"{one[N]}")

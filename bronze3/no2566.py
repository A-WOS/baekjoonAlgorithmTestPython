max_n = 0

for i in range(9):
    value = list(map(int, input().split()))

    if max(value) > max_n:
        max_n = max(value)  # 최댓값
        a = i + 1  # 행
        # index함수를 쓰면 max_n 값이 있으면 max_n의 위치 값을 돌려줌
        b = value.index(max_n) + 1

print(max_n)
print(a, b)

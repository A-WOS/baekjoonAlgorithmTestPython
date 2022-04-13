numbers = list(map(int, input().split()))
rs = ' '.join(map(str, numbers))
# numbers 가 1 2 3 4 5이면 while 탈출
while rs != '1 2 3 4 5':
    for i in range(len(numbers)-1):
        # n번째 수가 n + 1 번째 수보다 크면 스왑
        if numbers[i] > numbers[i+1]:
            temp = numbers[i]
            numbers[i] = numbers[i+1]
            numbers[i+1] = temp
            # 1 2 3 4 5 인지 확인하기 위해 rs 변수 사용
            rs = ' '.join(map(str, numbers))
            # 값이 바뀔 때마다 출력
            print(rs)

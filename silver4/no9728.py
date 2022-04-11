# 테스트 케이스 개수
from collections import Counter

T = int(input())

for cnt in range(T):
    N, M = map(int, input().split())
    # 오름차순이라고 했기 때문에 sorted로 정렬
    numbers = sorted(map(int, input().split()))
    rs = []
    # 투 포인터로 합산한 결과값 rs에 추가
    left, right = 0, len(numbers) - 1
    while left < right:
        rs.append(numbers[left] + numbers[right])
        left += 1
        right -= 1
    
    # counter 로 제일 많이 나온 수의 횟수 체크
    counter = Counter(rs)
    val = max(counter.values())
    print(f'Case #{cnt+1}: {val}')
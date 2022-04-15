import sys

N = int(input())
student_nums = []
for _ in range(N):
    student_num = sys.stdin.readline().rstrip()
    student_nums.append(student_num)

# 학생 번호를 다르게 만들 수 있는 자리수
index = list(range(-1, -(len(student_nums[0])+1), -1))

# 뒤부터 맞는게 있는지 확인
for j in index:
    # 각 자리수 마다 같은 수가 있는지 확인, 담기 위해 만들어진 temps 배열
    temps = []
    for i in range(len(student_nums)):
        temps.append(student_nums[i][j:])
    # set 으로 중복된 수를 제거, 배열의 길이와 집합의 길이가 같으면 중복된 수가 없다 판단
    if len(set(temps)) == len(list(temps)):
        # temps 에 들어가있는 요소들의 길이는 다 같기 때문에 그 중 0번째 원소의 길이 출력
        print(len(temps[0]))
        break

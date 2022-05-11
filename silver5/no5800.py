K = int(input())
for i in range(K):
    std_list = list(map(int, input().split()))
    std_n = std_list[0]
    students = std_list[1:]

    students.sort(reverse=True)

    max_gap = -1
    for j in range(len(students)-1):
        cal = students[j] - students[j+1]
        if max_gap < cal:
            max_gap = cal

    print(f'Class {i+1}')
    print(f'Max {max(students)}, Min {min(students)}, Largest gap {max_gap}')

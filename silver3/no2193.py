# 문제의 과정을 알 수 있음
# timeout #1
# n = int(input())
# cnt = 0
#
# for i in range(2 ** (n-1), 2 ** n):
#     bin_n = bin(i)[2:]
#     flag = True
#     print(bin_n)
#     for j in range(len(bin_n) - 1):
#         if bin_n[j] == bin_n[j + 1] == '1':
#             flag = False
#             break
#     if flag:
#         print(f'True : {bin_n}')
#         cnt += 1
# print(cnt)

# timeout #2
# def pb(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return pb(n-1) + pb(n-2)


numbers = [1, 1] * 88
for i in range(2, 90):
    numbers[i] = numbers[i-1] + numbers[i-2]

num = int(input())
print(numbers[num-1])

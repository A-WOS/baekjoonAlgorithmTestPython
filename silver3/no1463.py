# def divide_three(N):
#     cnt = 0
#     if N % 3 == 1:
#         N = N -1
#         cnt += 1
#     return [N // 3, N % 3]
#
#
# def divide_two(N):
#     return [N // 2, N % 2]
#
#
# N = int(input())
#
# print(divide_two(N))
# print(divide_three(N))
# while N > 1:
#     if N > 3 and divide_three(N)[1] == 0 and divide_two(N)[1] == 0:
#         print(divide_three(N)[0])
#         break
#     if divide_three(N)[1] == 1:
#         print(divide_three(N)[0])
#         break
#     elif divide_two(N)[1] == 1:
#         print(divide_two(N)[0])
#         break
#     elif divide_three(N)[1] == 0:
#         print(divide_three(N)[0])
#         break
#     elif divide_two(N)[1] == 0:
#         print(divide_two(N)[0])
#         break

# 해당 숫자에서 1을 뺐을때 2나 3으로 나누어지는지 확인


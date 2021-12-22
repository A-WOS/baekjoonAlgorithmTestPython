# # 운동 N분, 초기 맥박 m, 최대 맥박 M, 1분동안 운동후 X+T, 1분동안 휴식 후 M-R
# # 5분동안 운동
# # 초기 맥박 70, 최대 맥박 120
# # 25*5
# # 70+25+25 2분 운동 = 120
# # 휴식 120-15-15-15 3분 휴식 = 75
# # 75+25 1분 운동 = 100
# # 100-15-15 2분 휴식 = 70
# # 70+25+25 2분 운동 = 120
# # 2+3+1+2+2 = 10분
#
N, m, M, T, R = map(int, input().split())

# M = 120 >= 맥박
# m = 70 최저 맥박
tot, flag = m, False
if M < tot:

# x = m
# work, rest = 0, 0
# while True:
#     if m + T > M:
#         work, rest = 0, -1
#         break
#     else:
#         if N == 0:
#             break
#         elif N > 0:
#             if m <= x <= M:
#                 if
#                 N -= 1
#
#         # if m <= x < M:
#         #     x += T
#         #     N -= 1
#         #     work += 1
#         # elif x > M:
#         #     rest += 1
#         #     x -= R
#         # elif x < m:
#         #     x = m
#     # else:
#     #     print(-1)
# print(work + rest)

word = input().split('.')
board = []
# 폴리오미노 2개
polio_mino = ['AAAA', 'BB']
flag = True
for val in word:
    board.append(val)
for i in range(len(board)):

    # for val in polio_mino:
    for j in range(len(polio_mino)):
        # print(board[i], val)
        # print(len(board[i]), len(list(val)))

        # if len(board[i]) == len(val):
        rs = len(board[i]) % len(polio_mino[j])
        rs_A = rs // 4
        rs_B = rs % 4
        if rs_A and rs_B == 2:
            for k in range(rs_A)
            # board[i] = val
            # print(board[i], val)
            # print(len(board[i], len(val)))
        # elif len(board[i]) ==
        # else:
        #     flag = False
        #     break
print(board, sep='.')
    # if flag is False:
    #     print(-1)
    #     break


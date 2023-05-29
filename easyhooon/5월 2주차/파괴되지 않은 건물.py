def accumulate(board):
    # 가로 누적
    for i in range(len(board)):
        for j in range(1, len(board[0])):
            board[i][j] += board[i][j - 1]

    # 누적된 가로에 대한 세로 누적
    for i in range(1, len(board)):
        for j in range(len(board[0])):
            board[i][j] += board[i - 1][j]


def point_score(board, r1, c1, r2, c2, score):
    board[r1][c1] += score
    board[r1][c2 + 1] -= score
    board[r2 + 1][c1] -= score
    # 두번 뺐으므로 다시 더해줌
    board[r2 + 1][c2 + 1] += score


def solution(board, skill):
    answer = 0
    accumulated_board = [[0] * 1001 for _ in range(1001)]

    for t, r1, c1, r2, c2, degree in skill:
        score = degree
        if t == 1:
            score = -degree
        point_score(accumulated_board, r1, c1, r2, c2, score)

    accumulate(accumulated_board)

    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += accumulated_board[i][j]
            if board[i][j] > 0:
                answer += 1

    return answer
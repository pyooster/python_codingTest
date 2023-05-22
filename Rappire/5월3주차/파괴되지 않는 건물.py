def solution(board, skills):
    N = len(board)
    M = len(board[0])
    sumMap = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
    for type, r1, c1, r2, c2, degree in skills:
        if type == 1:
            degree = -degree
        sumMap[r1][c1] += degree
        sumMap[r1][c2 + 1] -= degree
        sumMap[r2 + 1][c1] -= degree
        sumMap[r2 + 1][c2 + 1] += degree

    # 누적합 가로
    for i in range(N):
        for j in range(M):
            sumMap[i][j + 1] += sumMap[i][j]

    # 누적합 세로
    for j in range(M):
        for i in range(N):
            sumMap[i + 1][j] += sumMap[i][j]

    answer = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] + sumMap[i][j] >= 1:
                answer += 1

    return answer

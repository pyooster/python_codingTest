# 스도쿠

import sys

si = sys.stdin.readline

row = [[False] * 10 for _ in range(10)] # i 번 행에 j라는 숫자가 이미 존재
col = [[False] * 10 for _ in range(10)] # i 열에 j 라는 숫자가 이미 존재
square = [[False] * 10 for _ in range(10)] # i번째 사각형에 j 라는 숫자가 존재
board = [[0] * 9 for _ in range(9)]


def dfs(cnt):
    x = cnt // 9
    y = cnt % 9
    if cnt == 81:
        for i in range(9):
            for j in range(9):
                print(board[i][j], end="")
            print()
        exit(0)

    if board[x][y] == 0:
        for i in range(1, 10):
            if not row[x][i] and not col[y][i] and not square[(x // 3) * 3 + (y // 3)][i]:
                row[x][i] = True
                col[y][i] = True
                square[(x // 3) * 3 + (y // 3)][i] = True
                board[x][y] = i

                dfs(cnt + 1)

                board[x][y] = 0
                row[x][i] = False
                col[y][i] = False
                square[(x // 3) * 3 + (y // 3)][i] = False
    else:
        dfs(cnt + 1)


for i in range(9):
    inp = si().strip()
    for j in range(9):
        board[i][j] = int(inp[j])
        if board[i][j] != 0:
            # print(board[i][j])
            row[i][board[i][j]] = True
            col[j][board[i][j]] = True
            square[(i // 3) * 3 + (j // 3)][board[i][j]] = True

dfs(0)
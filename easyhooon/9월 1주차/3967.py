# 매직스타
import sys

si = sys.stdin.readline

board = [list(si().strip()) for _ in range(5)]
positions = [
    (0, 4),
    (1, 1), (1, 3), (1, 5), (1, 7),
    (2, 2), (2, 6),
    (3, 1), (3, 3), (3, 5), (3, 7),
    (4, 4)
]
# 순서의 이유타
lines = [
    [positions[0], positions[2], positions[5], positions[7]],
    [positions[0], positions[3], positions[6], positions[10]],
    [positions[1], positions[2], positions[3], positions[4]],
    [positions[7], positions[8], positions[9], positions[10]],
    [positions[11], positions[9], positions[6], positions[4]],
    [positions[11], positions[8], positions[5], positions[1]]
]
filled = [False] * 12


def get_val(ch):
    return ord(ch) - ord('A') + 1


def validate():
    for line in lines:
        line_sum = 0
        for pos in line:
            line_sum += get_val(board[pos[0]][pos[1]])

        if line_sum != 26:
            return False

    return True


def dfs(idx):
    # 가지치기 추가


    if idx == 12:
        if validate():
            for row in board:
                print(''.join(row))
            exit(0)
        return

    x, y = positions[idx]
    if board[x][y] == 'x':
        for i in range(12):
            if not filled[i]:
                char = chr(ord('A') + i)
                filled[i] = True
                board[x][y] = char

                dfs(idx + 1)

                board[x][y] = 'x'
                filled[i] = False
    else:
        dfs(idx + 1)


# 이미 존재하는 알파벳 방문 체크
for i in range(5):
    for j in range(9):
        if 'A' <= board[i][j] <= 'L':
            filled[ord(board[i][j]) - ord('A')] = True

dfs(0)

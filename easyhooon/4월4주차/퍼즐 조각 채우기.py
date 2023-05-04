from collections import deque

dxs, dys = [-1, 0, 1, 0], [0, -1, 0, 1]


# def rotation(puzzle):
#     r = len(puzzle)
#     c = len(puzzle[0])
#     result = [[0] * r for _ in range(c)]
#     for i in range(r):
#         for j in range(c):
#             result[j][r - 1 - i] = puzzle[i][j]
#     return result


# 두개의 퍼즐을 인자로 받고 두개가 같은지 확인
def is_match(puzzle, emptyPuzzle):
    r = len(puzzle)
    c = len(puzzle[0])

    er = len(emptyPuzzle)
    ec = len(emptyPuzzle[0])

    if r != er or c != ec:
        return False

    for i in range(r):
        for j in range(c):
            if puzzle[i][j] != emptyPuzzle[i][j]:
                return False

    return True


# 퍼즐 모양을 포함 하는 가장 작은 직사각형을 만들어 주는 함수
def trans_puzzle(puzzle_location):
    x_min, x_max = 100, -1
    y_min, y_max = 100, -1

    for (x, y) in puzzle_location:
        x_min = min(x_min, x)
        x_max = max(x_max, x)
        y_min = min(y_min, y)
        y_max = max(y_max, y)

    x_len = x_max - x_min + 1
    y_len = y_max - y_min + 1

    trans = [[0] * y_len for _ in range(x_len)]

    for (x, y) in puzzle_location:
        trans[x - x_min][y - y_min] = 1

    return trans


def bfs(i, j, table, visited):
    puzzle = []
    n = len(table)
    q = deque()
    q.append((i, j))
    visited[i][j] = True
    puzzle.append((i, j))

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if not (0 <= nx < n and 0 <= ny < n):
                continue
            if not visited[nx][ny] and table[nx][ny] == 1:
                q.append((nx, ny))
                visited[nx][ny] = True
                puzzle.append((nx, ny))

    return puzzle


def solution(game_board, table):
    n = len(game_board)
    answer = 0
    puzzles = []
    # 빈 퍼즐 조각을 담아놓는 배열을 추가
    emptyPuzzles = []
    visited = [[False] * n for _ in range(n)]
    puzzle_sum = []

    for i in range(n):
        for j in range(n):
            if table[i][j] == 1 and not visited[i][j]:
                # 테이블 내에 각각의 퍼즐을 bfs 를 통해 찾아내고
                puzzle_location = bfs(i, j, table, visited)
                # 퍼즐 모양을 포함하는 가장 작은 직사각형을 만들어
                puzzle = trans_puzzle(puzzle_location)
                # 해당 직사각형을 퍼즐을 저장 하는 배열에 저장
                puzzles.append(puzzle)
                # 각 퍼즐의 칸 수도 따로 저장
                puzzle_sum.append(len(puzzle_location))

    # 이후 방문을 초기화하고 같은 작업을 게임보드에서 진행해서 빈 조각들을 emptyPuzzles에 저장
    visited = [[False] * n for _ in range(n)]

    # 앞에 만들어진 bfs함수와 똑같은 작업을 하기위해 게임보드의 0과 1을 뒤집음
    # 이제 빈 조각은 1로 표기
    for i in range(n):
        for j in range(n):
            game_board[i][j] = 0 if game_board[i][j] == 1 else 1

    # bfs를 게임보드에 실행하고 emptyPuzzles에 퍼즐 조각을 담음
    for i in range(n):
        for j in range(n):
            if game_board[i][j] == 1 and not visited[i][j]:
                puzzle_location = bfs(i, j, game_board, visited)
                puzzle = trans_puzzle(puzzle_location)
                emptyPuzzles.append(puzzle)

    # usedPuzzle 은 사용한 퍼즐을 알아보기 위한 배열
    usedPuzzle = [False for _ in range(len(puzzles) + 1)]

    for emptyPuzzle in emptyPuzzles:
        for idx, puzzle in enumerate(puzzles):
            # 이미 사용된 퍼즐이라면 넘어감
            if usedPuzzle[idx]:
                continue
            # 해당 퍼즐 조각이 들어갈 공간을 찾았을 때 확인하는 변수
            find = False
            for _ in range(4):
                # 시계 방향 회전
                # puzzle = rotation(puzzle)
                puzzle = list(zip(*puzzle[::-1]))

                # 게임 보드에 퍼즐을 추가할 수 있는지 확인
                if is_match(puzzle, emptyPuzzle):
                    # 찾았다면 퍼즐이 사용됬다고 기록하고
                    usedPuzzle[idx] = True
                    # 답을 추가하고
                    answer += puzzle_sum[idx]
                    # 이 빈 공간이 사용됬다고 표기
                    find = True
                    break

            # 퍼즐을 찾았으니 다음 빈공간으로 넘어감
            if find:
                break

    return answer


print(solution([[1, 1, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0], [0, 1, 1, 0, 0, 1], [1, 1, 0, 1, 1, 1], [1, 0, 0, 0, 1, 0], [0, 1, 1, 1, 0, 0]], [[1, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0], [1, 1, 0, 1, 1, 0], [0, 1, 0, 0, 0, 0]]))
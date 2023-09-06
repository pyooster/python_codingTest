# 마법사 상어와 토네이도
# 토네이도가 소멸되었을 때, 격자의 밖으로 나간 모래의 양을 구해보자.
import sys

si = sys.stdin.readline

n = int(si())

board = [list(map(int, si().split())) for _ in range(n)]
before_sand = 0
for i in range(n):
    for j in range(n):
        if board[i][j] > 0 :
            before_sand += board[i][j]

map_dir = [
    # 왼쪽(0, -1)
    [
        [0, 0, 2, 0, 0],볼
        [0, 10, 7, 1, 0],
        [5, -1, 0, 0, 0],
        [0, 10, 7, 1, 0],
        [0, 0, 2, 0, 0]
    ],
    # 아래쪽(1, 0)
    [
        [0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [2, 7, 0, 7, 2],
        [0, 10, -1, 10, 0],
        [0, 0, 5, 0, 0]
    ],
    # 오른쪽(0, 1)
    [
        [0, 0, 2, 0, 0],
        [0, 1, 7, 10, 0],
        [0, 0, 0, -1, 5],
        [0, 1, 7, 10, 0],
        [0, 0, 2, 0, 0]
    ],
    # 윗쪽(0, - 1)
    [
        [0, 0, 5, 0, 0],
        [0, 10, -1, 10, 0],
        [2, 7, 0, 7, 2],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0]
    ]
]

dxs, dys = [0, 1, 0, -1], [-1, 0, 1, 0]
x, y = n // 2, n // 2
# 이동 방향
move_dir = 0
# 이동 횟수
move_num = 1


def in_range(r, c):
    return 0 <= r < n and 0 <= c < n


def end():
    return not in_range(x, y)


def tornado(x, y, dx, dy):
    # 토네이도가 이동하는 곳의 모래의 원래 양
    total_sand = board[x][y]
    moved_sand = 0

    # before
    # for i in range(n):
    #     for j in range(n):
    #         print(board[i][j], end=" ")
    #     print()

    # 왼쪽
    if dx == 0 and dy == -1:
        d = 0
    # 아래
    elif dx == 1 and dy == 0:
        d = 1
    # 오른쪽
    elif dx == 0 and dy == 1:
        d = 2
    # 위
    elif dx == -1 and dy == 0:
        d = 3

    # 모래가 퍼짐
    # a 로 이동하는 모래의 양은 비율이 적혀있는 칸으로 이동하지 않은 남은 모래의 양과 같다.
    for i in range(5):
        for j in range(5):
            if map_dir[d][i][j] != 0:
                val = 0
                # a 의 위치 일 경우
                if map_dir[d][i][j] == -1:
                    # 아직 안 퍼진 모래 양을 계산
                    # val = total_sand - moved_sand
                    pass
                else:
                    # 해당 위치에 퍼짐 비율만큼 모래 양을 계산
                    val = (total_sand * map_dir[d][i][j]) // 100

                # 퍼진 모래의 총량 갱신
                moved_sand += val

                # 실제 퍼짐 위치 계산(문제의 원인 후보)
                # board 내에 좌표
                # 이게 아닌가
                nx = x + (i - 2)
                ny = y + (j - 2)

                if in_range(nx, ny):
                    # 퍼진 그 위치에 모래를 추가
                    board[nx][ny] += val


    # a 위치에 모래 양 계산
    a_sand = total_sand - moved_sand
    # # a 의 위치
    # if d == 0:
    #     a_x, a_y = x, y - 1
    # elif d == 1:
    #     a_x, a_y = x + 1, y
    # elif d == 2:
    #     a_x, a_y = x, y + 1
    # else:
    #     a_x, a_y = x - 1, y - 1
    a_x, a_y = x + dx, y + dy

    if in_range(a_x, a_y):
        # a 위치에 이미 모래가 존재할 수 있기 때문에 대입이 아니라 '추가'
        board[a_x][a_y] += a_sand
    # 원래 위치에 존재 했던 모래를 모두 제거
    board[x][y] -= total_sand
    # print("total_sand", total_sand)
    # print("moved_sand", moved_sand)

    # after
    # for i in range(n):
    #     for j in range(n):
    #         print(board[i][j], end=" ")
    #     print()


# 빙글 빙글 시뮬레이션
while not end():
    for _ in range(move_num):
        x, y = x + dxs[move_dir], y + dys[move_dir]
        if end():
            break
        else:
            # print(x, y)
            tornado(x, y, dxs[move_dir], dys[move_dir])

    move_dir = (move_dir + 1) % 4
    if move_dir == 0 or move_dir == 2:
        move_num += 1

after_sand = 0
for i in range(n):
    for j in range(n):
        if board[i][j] > 0:
            after_sand += board[i][j]

print(before_sand - after_sand)

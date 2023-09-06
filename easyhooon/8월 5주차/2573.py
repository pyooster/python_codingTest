# 빙산
# bfs 진행 -> 마을의 개수가 처음으로 2개 이상일때

import sys
from collections import deque

si = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def bfs(i, j):
    q = deque()
    q.append((i, j))

    while q:
        x, y = q.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if in_range(nx, ny) and not visited[nx][ny] and board[nx][ny] == 0:
                if board[x][y] > 0:
                    board[x][y] -= 1
            elif in_range(nx, ny) and not visited[nx][ny] and board[nx][ny] > 0:
                visited[nx][ny] = True
                q.append((nx, ny))


n, m = map(int, si().split())
board = [list(map(int, si().split())) for _ in range(n)]
time = 0


while True:
    visited = [[False] * m for _ in range(n)]
    cnt = 0

    for i in range(n):
        for j in range(m):
            if board[i][j] != 0 and not visited[i][j]:
                visited[i][j] = True
                bfs(i, j)
                cnt += 1

    # print(cnt)
    # for i in range(n):
    #     for j in range(m):
    #         print(board[i][j], end=" ")
    #     print()

    # 빙산이 처음으로 분리된 경우
    if cnt > 1:
        break

    # time 증가 
    time += 1

    # 빙산이 모두 녹았지만, 분리되지 않은 경우
    if cnt == 0:
        time = 0
        break

print(time)





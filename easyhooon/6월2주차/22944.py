# 죽음의 비

import sys
from collections import deque

# 모든 우산의 내구도는 d 로 동일
# 최단거리 문제이므로 항상 풀던대로 bfs
# 우산을 들고 있다가 파괴되 경우와 원래 부터 우산이 없는 경우를 분리? ㄴㄴ 우산의 내구도를 통해 판단 가능

si = sys.stdin.readline

dxs = [-1, 0, 1, 0]
dys = [0, -1, 0, 1]

n, h, d = map(int, si().split())
board = [list(si().strip()) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

sx, sy = 0, 0

for i in range(n):
    for j in range(n):
        if board[i][j] == 'S':
            sx, sy = i, j


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def bfs():
    q = deque([(sx, sy, h, 0, 0)])
    visited[sx][sy] = h

    while q:
        x, y, curr_h, curr_d, cnt = q.pop()

        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy

            if in_range(nx, ny):
                if board[nx][ny] == 'E':
                    print(cnt + 1)
                    return

                next_h = curr_h
                next_d = curr_d

                if board[nx][ny] == 'U':
                    next_d = d

                if next_d == 0:
                    next_h -= 1

                else:
                    # next_d 가 0 이 아닐때만 실행
                    next_d -= 1

                if next_h == 0:
                    continue

                if visited[nx][ny] < next_h:
                    visited[nx][ny] = next_h
                    q.appendleft((nx, ny, next_h, next_d, cnt + 1))

    print(-1)


bfs()

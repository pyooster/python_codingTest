# 토마토
import sys
from collections import deque

si = sys.stdin.readline

n, m = map(int, si().split())

graph = [list(map(int, si().split())) for _ in range(m)]
dist = [[-1] * n for _ in range(m)]
dxs = [-1, 0, 1, 0]
dys = [0, -1, 0, 1]

q = deque()

for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
            dist[i][j] = 0
            q.append((i, j))


def in_range(x, y):
    return 0 <= x < m and 0 <= y < n


def can_go(x, y):
    return in_range(x, y) and graph[x][y] != -1 and dist[x][y] == -1


def bfs():
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if can_go(nx, ny):
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))


bfs()

# print(graph)
# print(dist)

answer = -sys.maxsize
# 모든 토마토가 익지 않은 경우도 존재
for i in range(m):
    for j in range(n):
        # 방문하지 못한 토마토가 존재
        if dist[i][j] == -1 and graph[i][j] == 0:
            print(-1)
            exit(0)

        else:
            answer = max(answer, dist[i][j])

print(answer)










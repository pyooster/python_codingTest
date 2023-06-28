# 단순한 dfs/bfs 문제
from collections import deque

graph = [[0] * 101 for _ in range(101)]
visited = [[False] * 101 for _ in range(101)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def in_range(x, y, n, m):
    return 0 <= x < n and 0 <= y < m


def bfs(x, y, n, m):
    island_sum = 0

    q = deque()
    q.append((x, y))
    island_sum += graph[x][y]

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if in_range(nx, ny, n, m) and not visited[nx][ny] and graph[nx][ny] != 0:
                visited[nx][ny] = True
                island_sum += graph[nx][ny]
                q.append((nx, ny))

    return island_sum


def solution(maps):
    answer = []
    n = len(maps)
    m = len(maps[0])

    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'X':
                graph[i][j] = 0
            else:
                graph[i][j] = int(maps[i][j])

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and graph[i][j] != 0:
                visited[i][j] = True
                island_sum = bfs(i, j, n, m)
                answer.append(island_sum)

    answer.sort()

    if len(answer) == 0:
        answer.append(-1)

    return answer
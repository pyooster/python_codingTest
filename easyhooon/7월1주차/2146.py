# 다리 만들기 1
# 1. BFS or DFS 로 각각의 섬 다르게 넘버링 해주기
# 2. 두 섬을 잇는 최단거리의 다리를 찾는다

import sys
from collections import deque

si = sys.stdin.readline

# n <= 100
n = int(si())

graph = [list(map(int, si().split())) for _ in range(n)]
num_graph = [[0] * n for _ in range(n)]
visited1 = [[False] * n for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def inside(x, y, start_num):
    flag = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if in_range(nx, ny):
            if num_graph[nx][ny] != start_num:
                flag = False
                return flag

    return flag


def bfs1(i, j, cnt):
    q = deque()
    q.append((i, j))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if in_range(nx, ny) and not visited1[nx][ny] and graph[nx][ny] != 0:
                visited1[nx][ny] = True
                num_graph[nx][ny] = cnt
                q.append((nx, ny))


def bfs2(i, j, start_num):
    visited2 = [[False] * n for _ in range(n)]
    q = deque()
    q.append((i, j, 0))
    visited2[i][j] = True

    while q:
        x, y, cnt = q.popleft()
        if num_graph[x][y] != start_num and num_graph[x][y] != 0:
            # print(i, j, x, y)
            # print(num_graph[i][j], num_graph[x][y])
            # print(cnt)
            return cnt

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if in_range(nx, ny) and not visited2[nx][ny] and num_graph[nx][ny] != start_num:
                visited2[nx][ny] = True
                q.append((nx, ny, cnt + 1))

    return sys.maxsize


cnt = 0
for i in range(n):
    for j in range(n):
        if not visited1[i][j] and graph[i][j] != 0:
            visited1[i][j] = True
            cnt += 1
            num_graph[i][j] = cnt
            bfs1(i, j, cnt)

# print(num_graph)
# 최단 거리를 잇는 다리의 길이를 구하기
min_len = sys.maxsize

# 2개의 섬 씩 매칭을 시켜보면서 최단거리를 구해보자
# n 이 100이라 4중 포문까지 해도 됨
for i in range(1, cnt):
    for k in range(n):
        for l in range(n):
            if num_graph[k][l] == i:
                # 하지만 bfs 까지 들어가면 시간초과 -> 최적화 필요 (섬 외곽이 아닌 섬 내부점에서 시작할 경우 반드시 최소가 아님)
                if not inside(k, l, i):
                    # 굳이 여기서 start_num과 end_num 을 지정해야 하나?
                    # 시작점과 0이 아닌 다른 점에 도달했을때 그 최초의 거리를 구하면 되는건데(도착점이 어떤 섬인지와 관계 없이)
                    min_len = min(min_len, bfs2(k, l, i))

print(min_len - 1)


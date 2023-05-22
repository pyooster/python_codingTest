# 벽 부수고 이동하기 4
# 0: 이동 가능
# 1: 이동 할 수 없는 벽
# 이동하려면 두 칸이 인접해야 함
# 두 칸이 변을 공유할 때 인접하다고 함

# 벽을 부수고 이동할 수 있는 곳으로 변경
# 그 위치에서 이동할 수 있는 칸의 개수를 세어봄

# 원래 빈 칸인 곳은 0을 출력, 벽인 곳은 이동할 수 있는 칸의 개수를 10으로 나눈 나머지를 출력

# 101
# 010
# 101
#
# 303
# 050
# 303
#
# 11001
# 00111
# 01010
# 10101
#
# 46003
# 00732
# 06040
# 50403

import sys
from collections import deque

si = sys.stdin.readline

n, m = map(int, si().split())

dxs, dys = [-1, 0, 1, 0], [0, -1, 0, 1]

graph = [list(map(int, si().strip())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
zeros = [[0] * m for _ in range(n)]
group_num = 1
group_size = {}
group_size[0] = 0


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def can_go(x, y):
    return in_range(x, y) and not visited[x][y] and graph[x][y] == 0


def bfs(i, j):
    q = deque()
    q.append((i, j))
    cnt = 1
    while q:
        x, y = q.popleft()
        zeros[x][y] = group_num
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                visited[nx][ny] = True
                q.append((nx, ny))
                cnt += 1
    return cnt


for i in range(n):
    for j in range(m):
        if graph[i][j] == 0 and not visited[i][j]:
            visited[i][j] = True
            size = bfs(i, j)
            group_size[group_num] = size
            group_num += 1

for x in range(n):
    for y in range(m):
        if graph[x][y] == 1:
            # 그룹 중복 누적을 막기 위해
            temp = set()
            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                if in_range(nx, ny):
                    temp.add(zeros[nx][ny])

            for elem in temp:
                graph[x][y] += group_size[elem]
                graph[x][y] %= 10

for i in range(n):
    for j in range(m):
        print(graph[i][j], end="")
    print()
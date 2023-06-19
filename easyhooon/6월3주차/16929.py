import sys

sys.setrecursionlimit(10 ** 6)

si = sys.stdin.readline

n, m = map(int, si().split())

# set 으로 지나온 경로 담고 있는 건 메모리가 터질 것 같은데 n, m <= 50 이라
# 이전에 온 방향을 기억하면 어떨까? 그 역방향으로 가는거만 막으면 사이클 판단 가능할듯
# dfs 시작점일 경우엔 이전 방향이 없는데
graph = [list(si().strip()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dxs = [-1, 0, 1, 0]
dys = [0, -1, 0, 1]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def dfs(x, y, before_dx, before_dy):
    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy

        # 범위 밖, 다른 알파벳, 바로 이전 위치로 이동 하는 경우 cut
        if not in_range(nx, ny) or graph[x][y] != graph[nx][ny] or (dx == -before_dx and dy == -before_dy):
            continue

        # 바로 이전 위치로 이동하는 것이 아닌데 이미 방문한 곳에 도착하였다.
        # 사이클이 생성 되었다.
        if visited[nx][ny]:
            # print(nx, ny)
            print('Yes')
            exit(0)

        # print(nx, ny)
        visited[nx][ny] = True
        dfs(nx, ny, dx, dy)


for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            visited[i][j] = True
            dfs(i, j, 0, 0)
print('No')


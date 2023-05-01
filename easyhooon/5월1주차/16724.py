# 피리 부는 사나이
# 지도 어느 구역에 있더라도, 피리를 불때, SAFE ZONE 으로 들어갈 수 있게 하는  SAFE ZONE 의 '최소' 개수
# 순환 -> 사이클
# 격자 좌표가 있어서 유파일거라고 생각을 못했음 -> 격자 탐색 + 유파 (백조의 호수 쉬운 버전)

import sys

si = sys.stdin.readline

n, m = map(int, si().split())
graph = [list(si().strip()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
uf = [[(x, y) for y in range(m)] for x in range(n)]

# print(uf)

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]


def union(curr, next):
    x, y = find(curr[0], curr[1])
    nx, ny = find(next[0], next[1])

    uf[x][y] = (nx, ny)


def find(x, y):
    if (x, y) == uf[x][y]:
        return (x, y)

    uf[x][y] = find(uf[x][y][0], uf[x][y][1])
    return uf[x][y]


def dfs(x, y):
    global answer

    nx, ny = x, y
    if graph[x][y] == "U":
        nx, ny = x + dxs[0], y + dys[0]
    elif graph[x][y] == "D":
        nx, ny = x + dxs[1], y + dys[1]
    elif graph[x][y] == "L":
        nx, ny = x + dxs[2], y + dys[2]
    elif graph[x][y] == "R":
        nx, ny = x + dxs[3], y + dys[3]

    next_root = find(nx, ny)
    # 사이클이 아니라면
    if next_root == (nx, ny) and graph[nx][ny] != "C":
        union((x, y), (nx, ny))
        visited[nx][ny] = True
        dfs(nx, ny)

    else:
        # 새 사이클 형성
        if next_root == (x, y):
            graph[x][y] = "C"
            answer += 1
            return

        # 기존의 사이클에 포함
        else:
            union((x, y), (nx, ny))
            return

# 시이클의 개수
answer = 0

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            visited[i][j] = True
            dfs(i, j)

# print(graph)
print(answer)

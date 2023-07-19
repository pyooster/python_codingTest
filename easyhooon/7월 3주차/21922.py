from collections import deque
import sys

# 굳이 방문 배열을 3차원으로 관리 하지 않아도 된다.

si = sys.stdin.readline

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

n, m = map(int, si().split())
visited = [[0] * m for _ in range(n)]

q = deque()
graph = []

for i in range(n):
    line = list(map(int, si().split()))
    for j in range(m):
        # 에어컨 위치 미리 큐에 넣어 놓기
        if line[j] == 9:
            q.append((i, j))
            visited[i][j] = 1
    graph.append(line)


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def bfs():
    while q:
        x, y = q.popleft()

        for i in range(4):
            dx, dy = dxs[i], dys[i]
            nx, ny = x + dx, y + dy

            while in_range(nx, ny):
                # 방문 체크
                visited[nx][ny] = 1
                # 에어컨 위치로 이동한 경우
                if graph[nx][ny] == 9:
                    break
                # 방향 전환
                if graph[nx][ny] == 3:
                    dx, dy = -dy, -dx
                # 방향 전환
                elif graph[nx][ny] == 4:
                    dx, dy = dy, dx
                # 1, 2 물건을 정면으로 마주치는 바람 이동 종료
                elif (graph[nx][ny] == 1 and dx == 0) or (graph[nx][ny] == 2 and dy == 0):
                    break

                nx += dx
                ny += dy


bfs()

answer = 0
for i in range(n):
    for j in range(m):
        if visited[i][j] == 1:
            answer += 1

print(answer)

from collections import deque
n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
time, x, y = map(int, input().split())
q = deque()

for i in range(1, k+1):
    for col in range(n):
        for row in range(n):
            if graph[col][row] == i:
                q.append([col, row, 0])

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

while q:
    cx, cy, t = q.popleft()
    if t == time:
        continue

    for i in range(4):
        nx, ny = cx + dx[i], cy + dy[i]
        if nx in range(n) and ny in range(n) and graph[nx][ny] == 0:
            q.append([nx, ny, t+1])
            graph[nx][ny] = graph[cx][cy]
    
            
print(graph[x - 1][y - 1])

print()
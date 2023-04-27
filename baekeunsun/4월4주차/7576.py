# 토마토
from collections import deque

def bfs(M, N, box):
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    days = -1

    while ripe:
        days += 1
        for _ in range(len(ripe)):  # 하루
            x, y = ripe.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < N and 0 <= ny < M and box[nx][ny] == 0:
                    box[nx][ny] = 1
                    ripe.append([nx, ny])
                
    for b in box:
        if 0 in b:
            return -1
    return days


M, N = map(int, input().split())
box = list()
ripe = deque()

for i in range(N):
    row = list(map(int, input().split()))
    for j in range(M):
        if row[j] == 1:
            ripe.append([i, j])
    box.append(row)
    
print(bfs(M, N, box))

import sys
from collections import deque

input = sys.stdin.readline

move = [[1, 0], [-1, 0], [0, 1], [0, -1]]


N, H, D = list(map(int, input().split()))
grid = []
checklist = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    grid.append(list(input().rstrip()))

for i in range(N):
    for j in range(N):
        if grid[i][j] == "S":
            start = [i, j]
            break

queue = deque([[start[0], start[1], H, 0, 0]])
while queue:
    x, y, hp_b, umbrella_b, count = queue.pop()
    for dx, dy in move:
        dx += x
        dy += y
        hp = hp_b
        umbrella = umbrella_b
        if 0 <= dx < N and 0 <= dy < N:
            if grid[dx][dy] == "E":
                print(count + 1)
                sys.exit()

            if grid[dx][dy] == "U":
                umbrella = D

            if umbrella > 0:
                umbrella -= 1
            else:
                hp -= 1
                if hp == 0:
                    continue

            if checklist[dx][dy] < hp:
                checklist[dx][dy] = hp
                queue.appendleft([dx, dy, hp, umbrella, count + 1])

print(-1)

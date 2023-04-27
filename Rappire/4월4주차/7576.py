import sys
from collections import deque

input = sys.stdin.readline

move = [[1, 0], [-1, 0], [0, 1], [0, -1]]


M, N = map(int, input().split())
count_arr = [[0 for _ in range(M)] for _ in range(N)]
arr = []

for i in range(N):
    arr.append(list(map(int, input().split())))
queue = deque([])
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            queue.append([i, j, 1])


while len(queue) > 0:
    now = queue.popleft()
    x, y, num = now
    for dx, dy in move:
        dx += x
        dy += y
        if dx >= 0 and dx < N and dy >= 0 and dy < M:
            if arr[dx][dy] == 0:
                queue.append([dx, dy, num + 1])
                arr[dx][dy] = num + 1
            # 필요 없었던 코드
            # elif arr[dx][dy] == -1:
            #     pass
            # elif arr[dx][dy] > num + 1:
            #     queue.append([dx, dy, num + 1])
            #     arr[dx][dy] = num + 1
 
maxnum = -1
for line in arr:
    for i in line:
        if i == 0:
            print(-1)
            sys.exit()
        maxnum = max(maxnum, i)
print(maxnum - 1)

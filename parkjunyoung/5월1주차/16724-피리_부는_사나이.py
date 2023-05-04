# 피리 부는 사나이


d = {'U': [-1, 0], 'D': [1, 0], 'L': [0, -1], 'R': [0, 1]}
N, M = map(int, input().split())
pan = []
for i in range(N):
    arr = list(input())
    pan.append(arr)
# for i in pan:
#     print(i)
visited = [[-1 for _ in range(M)] for _ in range(N)]
ans = 0
cnt = 0


def dfs(x, y, cnt):
    global ans
    if visited[x][y] != -1:                # 방문을 했는데
        if visited[x][y] == cnt:           # 지금이랑 같은 싸이클이면
            ans += 1                       # + 1
        return                             # 멈춰
    visited[x][y] = cnt                    # 현재 싸이클
    dir = d[pan[x][y]]                     # 방향
    nx = x + dir[0]
    ny = y + dir[1]
    if 0 <= nx < N and 0 <= ny < M:        # 범위 안이면
        dfs(nx, ny, cnt)                   # 싸이클 돌기


for i in range(N):
    for j in range(M):
        if visited[i][j] == -1:            # 방문 체크
            dfs(i, j, cnt)
            cnt += 1

# for i in visited:
#     print(i)

print(ans)
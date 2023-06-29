# Two Dots
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())
pan = []
for i in range(N):
    temp = list(input())
    pan.append(temp)

flag = 0
# for i in pan:
#     print(i)


def dfs(x,y, start, color, cnt):
    global flag
    # 시작 위치랑 같고 4번이상움직였으면 사이클이 되는거
    if x == start[0] and y == start[1] and cnt >= 4:
        flag = 1
        return flag

    if flag:
        return

    visited[x][y] = 1
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < N and 0 <= ny < M:
            # 방문하지 않았고 같은 색이면 계속 이동
            if visited[nx][ny] == 0 and color == pan[nx][ny]:
                dfs(nx, ny, start, color, cnt+1)
            # 방문했으면
            elif visited[nx][ny] == 1:
                # 시작위치고 4번이상이면
                if nx == start[0] and ny == start[1] and cnt >= 4:
                    flag = 1
                    return
    return


for i in range(N):
    for j in range(M):
        visited = [[0 for _ in range(M)] for _ in range(N)]
        visited[i][j] = 1
        start = [i, j]
        color = pan[i][j]
        dfs(i, j, start, color, 1)

if flag:
    print("Yes")
else:
    print("No")
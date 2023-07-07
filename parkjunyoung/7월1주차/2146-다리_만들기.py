# 다리 만들기

from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N = int(input())
pan = []
for i in range(N):
    temp = list(map(int, input().split()))
    pan.append(temp)

# 섬을 구분하기 위해서 cnt 부여
def island(x, y, cnt):
    q = deque()
    q.append((x, y))
    check[x][y] = cnt
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < N:
                if check[nx][ny] == 0:
                    if pan[nx][ny] != 0:
                        check[nx][ny] = cnt
                        q.append((nx, ny))


check = [[0 for _ in range(N)] for _ in range(N)]
cnt = 1
for i in range(N):
    for j in range(N):
        if pan[i][j] != 0 and check[i][j] == 0:
            island(i, j, cnt)
            cnt += 1

# 각 섬에서 출발해서 다른섬까지의 거리를 구한다
def bfs(q, my_num):
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            # 범위 안에 있고
            if 0 <= nx < N and 0 <= ny < N:
                # 다른 섬일때
                if pan[nx][ny] == 1 and check[nx][ny] != my_num:
                    return visitied[x][y]
                # 바다면서 방문하지 않았을때
                if check[nx][ny] == 0 and visitied[nx][ny] == -1:
                    visitied[nx][ny] = visitied[x][y] + 1
                    q.append((nx, ny))

# 최솟값 변수
min_ans = 10001

# 섬을 돌면서
for c in range(1, cnt):
    q = deque()
    visitied = [[-1 for _ in range(N)] for _ in range(N)]

    # 여기가 제일 문제였는데 모든섬의 값을 q에 먼저 넣어서 섬의 모든 점에서 부터 시작하는 걸로 변경하였다.
    # 그래야 최소값을 구할때 오류가 안생기는듯
    for i in range(N):
        for j in range(N):
            if check[i][j] == c:
                q.append((i, j))
                visitied[i][j] = 0

    # 거리를 구하고 최솟값이랑 비교
    ans = bfs(q, c)
    min_ans = min(ans, min_ans)

print(min_ans)
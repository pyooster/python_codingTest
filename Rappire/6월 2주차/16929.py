import sys

move = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def dfs(x, y, now, count):
    if visit[x][y] == 1 and count > 3:
        print("Yes")
        sys.exit()

    for dx, dy in move:
        dx += x
        dy += y
        if 0 <= dx < N and 0 <= dy < M:
            if mapArr[dx][dy] == now:
                if visit[dx][dy] == 0:
                    visit[dx][dy] = 1
                    dfs(dx, dy, now, count + 1)
                    visit[dx][dy] = 0


input = sys.stdin.readline

N, M = list(map(int, input().split()))
mapArr = [list(input().rstrip()) for _ in range(N)]
visit = [[0 for _ in range(M)] for _ in range(N)]


for i in range(N):
    for j in range(M):
        now = mapArr[i][j]
        if visit[i][j] == 0:
            dfs(i, j, now, 0)

print("No")

import sys

input = sys.stdin.readline
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def check(x, y):
    if checkArr[x][y] == 1:
        return False
    for dx, dy in move:
        nx = x + dx
        ny = y + dy
        if checkArr[nx][ny] == 1:
            return False
    return True


def dfs(visitCount, cost):
    global answer
    if cost >= answer:
        return
    if visitCount == 3:
        answer = min(answer, cost)
    else:
        for i in range(1, N - 1):
            for j in range(1, N - 1):
                if check(i, j):
                    temp_cost = mapArr[i][j]
                    for di, dj in move:
                        ni = di + i
                        nj = dj + j
                        checkArr[ni][nj] = 1
                        temp_cost += mapArr[ni][nj]
                    dfs(visitCount + 1, cost + temp_cost)
                    for di, dj in move:
                        ni = di + i
                        nj = dj + j
                        checkArr[ni][nj] = 0


N = int(input())
answer = int(10e9)
mapArr = [list(map(int, input().split())) for _ in range(N)]
checkArr = [[0 for _ in range(N)] for _ in range(N)]
dfs(0, 0)
print(answer)

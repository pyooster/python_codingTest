# 꽃길
# 꽃잎이 닿게 될 경우 두 꽃 모두 죽어버린다, 화단에 꽃잎이 나가버려도
# 서로 다른 세 씨앗이 모두 꽃 피게 하면서 가장 싼 각겨에 화단을 대여
# 꽃 하나당 5평
import sys

INT_MAX = sys.maxsize

si = sys.stdin.readline

n = int(si())
graph = [list(map(int, si().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

flower = []
# 꽃 씨앗의 위치를 정하고
# 겹치지 않게 잘 심었으면 최솟값 갱신

min_cost_sum = INT_MAX

dxs = [-1, 0, 1, 0]
dys = [0, -1, 0, 1]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def can_seed(x, y):
    flag = True
    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy
        if not in_range(nx, ny) or visited[nx][ny]:
            flag = False
            return flag

    return flag


def get_cost_sum():
    cost_sum = 0
    for (x, y) in flower:
        cost_sum += graph[x][y]
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            cost_sum += graph[nx][ny]

    return cost_sum


def dfs(curr_num):
    global min_cost_sum
    if curr_num == 3:
        # print(flower, get_cost_sum())
        min_cost_sum = min(min_cost_sum, get_cost_sum())
        return

    for i in range(n):
        for j in range(n):
            if not visited[i][j] and can_seed(i, j):
                visited[i][j] = True
                for di, dj in zip(dxs, dys):
                    ni = i + di
                    nj = j + dj
                    visited[ni][nj] = True

                flower.append((i, j))
                dfs(curr_num + 1)
                flower.pop()

                visited[i][j] = False
                for di, dj in zip(dxs, dys):
                    ni = i + di
                    nj = j + dj
                    visited[ni][nj] = False


dfs(0)
print(min_cost_sum)
# 꽃길

import sys
sys.setrecursionlimit(10**6)

N = int(input())
pan = []
for i in range(N):
    temp = list(map(int, input().split()))
    pan.append(temp)
visited = [[0 for _ in range(N)] for _ in range(N)]
dx = [0, 1, 0, -1, 0]
dy = [0, 0, 1, 0, -1]


def check(x, y):
    for d in range(5):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < N and 0 <= ny < N:
            if visited[nx][ny] == 1:
                return 0
    return 1


def hap(x, y):
    cost = 0
    for d in range(5):
        nx = x + dx[d]
        ny = y + dy[d]
        cost += pan[nx][ny]
    return cost


def dfs(cnt, cost_hap):
    global min_ans
    if cnt == 3:
        min_ans = min(min_ans, cost_hap)
        return
    for x in range(1, N-1):
        for y in range(1, N-1):
            if check(x, y) == 1:
                for d in range(5):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    visited[nx][ny] = 1
                dfs(cnt+1, cost_hap + hap(x, y))
                for d in range(5):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    visited[nx][ny] = 0

min_ans = 3001
dfs(0, 0)

print(min_ans)
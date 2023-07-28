# 알파벳
import sys
input = sys.stdin.readline

R, C = map(int, input().split())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

pan = []
for i in range(R):
    temp = list(input())
    pan.append(temp)

# for i in pan:
#     print(i)

visited = [0 for _ in range(26)]
visited[ord(pan[0][0])-65] = 1
max_cnt = 0
# print(visited)


def dfs(x, y, cnt):
    global max_cnt
    if cnt >= max_cnt:
        max_cnt = cnt
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < R and 0 <= ny < C:
            if visited[ord(pan[nx][ny])-65] == 0:
                visited[ord(pan[nx][ny])-65] = 1
                dfs(nx, ny, cnt + 1)
                visited[ord(pan[nx][ny])-65] = 0


dfs(0, 0, 1)
# for i in visited:
#     print(i)
print(max_cnt)
# print(len(check_alpha))
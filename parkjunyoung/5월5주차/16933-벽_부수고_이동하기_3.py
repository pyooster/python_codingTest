# 벽 부수고 이동하기 3

import sys
input = sys.stdin.readline
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
queue = deque()


def bfs():
    queue.append((0, 0, 0, 1))   # 0,0 좌표, 0 뿌순수 1 날짜
    flag = True                  # 낮, false = 밤

    while queue:
        for _ in range(len(queue)):  # 벽에 막혔을때 q의 길이 만큼하지 않으면 꼬인다
            x, y, k, ans = queue.popleft()
            if x == N-1 and y == M-1:
                return ans
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < M:
                    # 벽이 아닐때
                    if wall[nx][ny] == '0' and visited[nx][ny][k] == 0:
                        visited[nx][ny][k] = 1
                        queue.append((nx, ny, k, ans+1))
                    # 벽일때
                    if wall[nx][ny] == '1' and K > k and visited[nx][ny][k+1] == 0:
                    # 조건이 앞에 있나 뒤에 있나에 따라 range 에러가 발생...
                        if flag == True:
                            visited[nx][ny][k+1] = 1
                            queue.append((nx, ny, k+1, ans+1))
                        elif flag == False:
                            queue.append((x, y, k, ans+1))
        flag = not flag
    return -1


N, M, K = map(int, input().split())
wall = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
visited = [[[0] * (K + 1) for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1
print(bfs())
# for i in wall:
#     print(i)
# for i in visited:
#     print(i)


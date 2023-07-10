# 무인도 여행

from collections import deque


def solution(maps):
    answer = []
    N = len(maps)
    M = len(maps[0])
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    visited = [[0 for _ in range(M)] for _ in range(N)]


    # 방문 처리하면서 bfs
    def bfs(i, j):
        q = deque()
        q.append((i, j))
        visited[i][j] = 1
        # 식량의 총합
        hap = int(maps[i][j])
        while q:
            x, y = q.popleft()
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                # 범위안에 있고
                if 0 <= nx < N and 0 <= ny < M:
                    # 바다가 아니거나 방문하지 않았으면
                    if maps[nx][ny] != 'X' and visited[nx][ny] == 0:
                        visited[nx][ny] = 1
                        # 식량의 총합 추가
                        hap += int(maps[nx][ny])
                        q.append((nx, ny))
        return hap


    for i in range(N):
        for j in range(M):
            # 바다가 아니거나 방문하지 않았으면
            if maps[i][j] != 'X' and visited[i][j] == 0:
                # 탐색
                temp = bfs(i, j)
                answer.append(temp)

    # 오름차순으로 정렬
    answer.sort()

    # 답이 없다면 -1 출력
    if answer:
        return answer
    else:
        return [-1]



print(solution(["X591X", "X1X5X", "X231X", "1XXX1"]))
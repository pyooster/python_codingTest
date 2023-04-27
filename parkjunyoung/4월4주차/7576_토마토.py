# 토마토

from collections import deque

dr = [1, 0, -1, 0]                                                   # 하좌상우
dc = [0, -1, 0, 1]


def bfs():                                                           # bfs 함수
    while queue:                                                     # q 가 있으면
        r, c = queue.popleft()                                       # pop 하고
        for d in range(4):                                           # 방향 정해서
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < M and tomato[nr][nc] == 0:  # 값이 0 일때
                tomato[nr][nc] = tomato[r][c] + 1                    # 1씩 추가하고
                queue.append((nr, nc))                               # q 에 추가 하고


M, N = map(int, input().split())                                     # 상자 크기 입력
tomato = []                                                          #
for i in range(N):
    mato = list(map(int, input().split()))                           # 토마토 상태 입력
    tomato.append(mato)
queue = deque()                                                      # q 를 여기서 안하면 bfs 돌릴때 1이 여러개일때 찾지 못햇음
for i in range(N):                                                   # 상자를 다돌며
    for j in range(M):
        if tomato[i][j] == 1:                                        # 1 이 있다면
            queue.append((i, j))                                     # q 에 추가
bfs()                                                                # bfs 를 돌린다.
min_day = 0                                                          # 최소 날짜
ans = 0                                                              # -1 일 경우
for i in tomato:                                                     # 전체 탐색
    for j in i:
        if j == 0:                                                   # 0 이 있다면
            ans = -1                                                 # 모두 안익어서 -1
            break                                                    # 멈춰
        else:                                                        # 0이 없으면
            min_day = (max(min_day, j))                              # 최대값을 갱신하면서 저장한다
if ans == -1:                                                        # ans -1 이면
    print(-1)                                                        # 모두안익어서 -1 출력
else:
    print(min_day-1)                                                 # 최소날짜에서 1빼기

for i in tomato:
    print(i)
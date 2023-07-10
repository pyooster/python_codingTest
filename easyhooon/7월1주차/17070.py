# 파이프 옮기기
# 파이프가 밀 수 있는 방향은 총 3가지 오른, 아래, 오른 아래 대각
# 밀면서 회전 시킬 수 있음 회전은 45도로만 가능
# 미는 방향은 오른쪽, 아래 또는 오른족 아래 대각선 방향
# 파이프의 한쪽 끝을 (n, n)으로 이동시키는 방법의 개수를 구하라
# 시작점 (1,1) 1,2) 로 fix
# 이동시킬 수 없는 경우 0을 출력
# dp[i,j,k] := 파이프의 끝점이 (i, j) 로 k 방향으로 도착할 수 있는 경우의 수
# 벽이 존재 -> 벽이 있으면 이동 불가
# dfs 로 풀면 시간 초과 3^(n^n)
import sys

si = sys.stdin.readline

n = int(si())

graph = [list(map(int, si().split())) for _ in range(n)]
dp = [[[0] * 3 for _ in range(n)] for _ in range(n)]
dist = [[0] * n for _ in range(n)]

# 기저
# 90도 꺾을 수 없기 때문에 모든 열의 0, 1 번 칸으론 이동 불가능
# 이전 위치의 방향도 알 필요가 있음 -> 따라서 3차원으로
# 0: 오른쪽, 1: 대각선, 2: 아래
# 파이프의 길이가 존재, 파이프의 머리의 위치 -> 현재 위치의 k 값을 통해 파이프의 머리 위치는 확정
# 대각으로 이동할때 대각선칸만 0이면 되는게 아니라 오른, 아래 모두 0이 아니여야 한다.
# 벽이 있을 경우의 대한 처리
for i in range(1, n):
    if graph[0][i] == 1:
        break
    else:
        dp[0][i][0] = 1

for i in range(1, n):
    for j in range(2, n):
        for k in range(3):
            if graph[i][j] == 0:
                if k == 0:
                    dp[i][j][k] += dp[i][j - 1][0]
                    # if graph[i - 1][j] == 0 and graph[i][j - 1] == 0:
                    dp[i][j][k] += dp[i][j - 1][1]

                elif k == 1:
                    if graph[i - 1][j] == 0 and graph[i][j - 1] == 0:
                        dp[i][j][k] += dp[i - 1][j - 1][0] + dp[i - 1][j - 1][1] + dp[i - 1][j - 1][2]

                elif k == 2:
                    dp[i][j][k] += dp[i - 1][j][2]
                    # if graph[i - 1][j] == 0 and graph[i][j - 1] == 0:
                    dp[i][j][k] += dp[i - 1][j][1]

# print(dp[n - 1][n - 1])
print(sum(dp[n - 1][n - 1]))

# for i in range(n):
#     for j in range(n):
#         dist[i][j] = sum(dp[i][j])
#
# for i in range(n):
#     for j in range(n):
#         print(dist[i][j], end=" ")
#     print()

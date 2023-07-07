# RGB 거리

import sys

si = sys.stdin.readline

n = int(si())

board = [list(map(int, si().split())) for _ in range(n)]
dp = [[0] * 3 for _ in range(n)]

# 동등한 상황
# 지금까지 고려한 위치가 같고
# 현재 고른 위치가 같으며
# 현재 까지의 합이 같은 경우
# -> 지금까지 고려한 위치와 마지막에 고른 위치가 같다면 합이 작을수록 좋다
# dp[i][j]:= i번째 위치까지 선택하였고, 마지막에 j번 색깔을 선택 했을 때 최소 합

# 기저 조건
for i in range(0, 3):
    dp[0][i] = board[0][i]

for i in range(1, n):
    for j in range(0, 3):
        dp[i][j] = min(dp[i - 1][(j + 1) % 3], dp[i - 1][(j + 2) % 3]) + board[i][j]

print(min(dp[n - 1][0], dp[n - 1][1], dp[n - 1][2]))

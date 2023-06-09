# RGB 거리 역방향 풀이

import sys

si = sys.stdin.readline

n = int(si())

board = [list(map(int, si().split())) for _ in range(n)]
dp = [[0] * 3 for _ in range(n)]

# 기저 조건
dp[n - 1][0] = board[n - 1][0]
dp[n - 1][1] = board[n - 1][1]
dp[n - 1][2] = board[n - 1][2]

# 역방향으로 dp 배열 채우기
for i in range(n - 2, -1, -1):
    for j in range(0, 3):
        dp[i][j] = min(dp[i + 1][(j + 1) % 3], dp[i + 1][(j + 2) % 3]) + board[i][j]

print(min(dp[0][0], dp[0][1], dp[0][2]))

import sys

input = sys.stdin.readline

N = int(input())
dp = [[0, 0, 0] for _ in range(N + 1)]
for i in range(1, N + 1):
    R, G, B = list(map(int, input().split()))
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + R
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + G
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + B

print(min(dp[N]))

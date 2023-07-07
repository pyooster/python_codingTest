# 파이프 옮기기1

N = int(input())
home = []
for _ in range(N):
    temp = list(map(int, input().split()))
    home.append(temp)

dp = [[[0] * N for _ in range(N)] for _ in range(3)]
# 0 가로 1 세로 2 대각
dp[0][0][1] = 1


# 1번행 채우기?
for i in range(2, N):
    if home[0][i] == 0:
        dp[0][0][i] = dp[0][0][i-1]


for i in range(1, N):
    for j in range(1, N):
        if home[i][j] == 0:
            # 가로 = 가로랑 대각
            dp[0][i][j] = dp[0][i][j-1] + dp[2][i][j-1]
            # 세로 = 세로랑 대각
            dp[1][i][j] = dp[1][i-1][j] + dp[2][i-1][j]

        if home[i][j] == 0 and home[i-1][j] == 0 and home[i][j-1] == 0:
            # 대각 = 가로 세로 대각
            dp[2][i][j] = dp[0][i-1][j-1] + dp[1][i-1][j-1] + dp[2][i-1][j-1]
# print(dp)

ans = dp[0][N-1][N-1] + dp[1][N-1][N-1] + dp[2][N-1][N-1]

print(ans)
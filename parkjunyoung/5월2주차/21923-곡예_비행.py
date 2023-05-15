# 곡예 비행

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
score = []
for i in range(N):
    temp = list(map(int, input().split()))
    score.append(temp)
dp = [[-10000000001 for _ in range(M)] for _ in range(N)]
dp[N-1][0] = 0

# for i in score:
#     print(i)
# 상승
for j in range(M):
    for i in range(N-1, -1, -1):
        if i != N-1:                  # 위쪽
            dp[i][j] = dp[i+1][j]
        if j != 0:                    # 오른쪽
            dp[i][j] = max(dp[i][j], dp[i][j-1])
        dp[i][j] += score[i][j]


# print('---------------------')
# for i in dp:
#     print(i)

# 하강
for j in range(M):
    for i in range(N):
        if i != 0:                    # 아래쪽
            dp[i][j] = max(dp[i][j], dp[i-1][j])
        if j != 0:                    # 오른쪽
            dp[i][j] = max(dp[i][j], dp[i][j-1])
        dp[i][j] += score[i][j]

ans = 0
# print('---------------------')
# for i in dp:
#     print(i)


print(dp[N-1][M-1])

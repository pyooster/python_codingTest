# 곡예 비행
import sys
input = sys.stdin.readline
 
N, M = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
dp = [[-10000000001] * (M) for _ in range(N)]
dp[N-1][0] = 0

# 상승
for i in range(N-1,-1,-1):
    for j in range(M):
        if i != N - 1: # 밑에서 올라온 값 갱신
            dp[i][j] = dp[i+1][j]
        if j != 0 : # 왼쪽에서 이동한값 갱신
            dp[i][j] = max(dp[i][j], dp[i][j-1])

        dp[i][j] += Map[i][j]
 
# 하강
for i in range(N):
    for j in range(M):
        if i != 0 : # 위에서 내려온 값 갱신
            dp[i][j] = max(dp[i][j], dp[i-1][j])
        if j != 0 : # 왼쪽에서 이동한 값 갱신
            dp[i][j] = max(dp[i][j], dp[i][j-1])

        dp[i][j] += Map[i][j]
 
 
print(dp[N-1][M-1])

# 목장 건설하기
import sys

INT_MIN = -sys.maxsize

si = sys.stdin.readline

m, n = map(int, si().split())
graph = [list(map(int, si().split())) for _ in range(m)]

# for i in range(m):
#     for j in range(n):
#         print(graph[i][j], end = " ")
#     print()

# 완탐 1000^4 -> 시간 부족 -> dp 아닐끼? 추론
# dp[i][j] := (i,j)를 오른쪽 아래 꼭짓점으로 하는 가장 큰 정사각형의 한변의 길이
# 이미 아는 계산은 dp 배열에 저장
dp = [[0] * n for _ in range(m)]

max_length = INT_MIN

# 기저조건
for i in range(m):
    if graph[i][0] == 0:
        dp[i][0] = 1
        max_length = 1

for j in range(n):
    if graph[0][j] == 0:
        dp[0][j] = 1
        max_length = 1

# 점화식 채우기
for i in range(1, m):
    for j in range(1, n):
        if graph[i][j] == 0:
            # 왼쪽, 위, 왼쪽 대각선 위의 최소값 + 1을 현재 위치의 값으로 설정
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
            max_length = max(max_length, dp[i][j])

print(max_length)

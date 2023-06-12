import sys

si = sys.stdin.readline

dxs = [1, 0]
dys = [0, 1]

n, m = map(int, si().split())
k = int(si())

construct = set()

for _ in range(k):
    sx, sy, ex, ey = map(int, si().split())
    construct.add((sx, sy, ex, ey))
    construct.add((ex, ey, sx, sy))

# dp[i][j] := i, j 까지 도달할 수 있는 가지 수
dp = [[0] * (m + 1) for _ in range(n + 1)]

# 초기 조건에 길이 막히면 그 이후로 채우면 안됨
# 여기가 인덱스 문제가 있는 듯(틀린 이유)
# for i in range(n + 1):
#     if (i, 0, i + 1, 0) in construct:
#         break
#     else:
#         dp[i][0] = 1
#
# for j in range(m + 1):
#     if (0, j, 0, j + 1) in construct:
#         break
#     else:
#         dp[0][j] = 1

dp[0][0] = 1
# 초기 조건에 길이 막히면 그 이후로 채우면 안됨
for i in range(1, n + 1):
    if (i - 1, 0, i, 0) in construct:
        break
    else:
        dp[i][0] = 1
for j in range(1, m + 1):
    if (0, j - 1, 0, j) in construct:
        break
    else:
        dp[0][j] = 1

# 1. 위에서 내려오는 거
# 2. 왼쪽에서 오른쪽
# 탑 다운이 더 직관적일 것 같은데..
for i in range(1, n + 1):
    for j in range(1, m + 1):
        # (이동 시작 지점과 이동 후 지점이 모두 공사 중일 경우) 가 아닌 경우
        if not ((i - 1, j, i, j) in construct):
            dp[i][j] += dp[i - 1][j]
        if not ((i, j - 1, i, j) in construct):
            dp[i][j] += dp[i][j - 1]

print(dp[n][m])

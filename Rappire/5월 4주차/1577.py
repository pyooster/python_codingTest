import sys
from collections import defaultdict

input = sys.stdin.readline


def makeHash(startX, startY):
    return str(startX) + "," + str(startY)


N, M = map(int, input().split())
K = int(input())

road = defaultdict(list)
dp = [[0 for _ in range(M + 2)] for _ in range(N + 2)]
dp[1][1] = 1
for i in range(K):
    startX, startY, endX, endY = list(map(int, input().split()))
    road[makeHash(startX + 1, startY + 1)].append([endX + 1, endY + 1])
    road[makeHash(endX + 1, endY + 1)].append([startX + 1, startY + 1])

for i in range(1, N + 2):
    for j in range(1, M + 2):
        if [i, j] not in road[makeHash(i - 1, j)]:
            dp[i][j] += dp[i - 1][j]
        if [i, j] not in road[makeHash(i, j - 1)]:
            dp[i][j] += dp[i][j - 1]

print(dp[N + 1][M + 1])

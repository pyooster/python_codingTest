import sys

input = sys.stdin.readline
C, N = map(int, input().split())
arr = []
maxint = int(10e10)
dp = [maxint for _ in range(C + 1)]
dp[0] = 0
for i in range(N):
    arr.append(list(map(int, input().split())))

for i in range(C + 1):
    for cost, j in arr:
        now = i + j
        if now > C:
            now = C
        dp[now] = min(dp[now], dp[i] + cost)

print(dp[-1])

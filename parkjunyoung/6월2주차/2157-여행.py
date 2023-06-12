# 여행

N, M, K = map(int, input().split())
food = [[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(K):
    a, b, c = map(int, input().split())
    if food[a][b] != 0:
        food[a][b] = max(food[a][b], c)
    else:
        food[a][b] = c

dp = [[-1 for _ in range(301)] for _ in range(301)]


def func(i, cnt):
    if i != 1 and cnt == 1:
        return -9999999
    if i == 1:
        return 0
    if dp[i][cnt] != -1:
        return dp[i][cnt]
    dp[i][cnt] = -9999999
    for j in range(1, i):
        if food[j][i]:
            dp[i][cnt] = max(dp[i][cnt], func(j, cnt - 1) + food[j][i])

    return dp[i][cnt]


print(func(N, M))

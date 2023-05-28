# 도로의 개수

N, M = map(int, input().split())
k = int(input())

# visited = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
dp[0][0] = 1

stop = []
for _ in range(k):
    a, b, c, d = map(int, input().split())
    stop.append(((a, b), (c, d)))


# for i in stop:
#     print(i)

dp[0][0] = 1

move = [(1, 0), (0, 1)]
for x in range(N + 1):
    for y in range(M + 1):
        for i in range(2):
            nx = x + move[i][0]
            ny = y + move[i][1]
            if nx <= N and ny <= M:
                if ((x, y), (nx, ny)) in stop or ((nx, ny), (x, y)) in stop:
                    continue
                else:
                    dp[nx][ny] += dp[x][y]
                # print(x,y)

for i in dp:
    print(i)

print(dp[N][M])
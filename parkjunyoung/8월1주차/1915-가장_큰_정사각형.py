# 가장 큰 정사각형

n, m = map(int, input().split())
pan = []
for _ in range(n):
    row = input()
    pan.append([int(ch) for ch in row])

dp = [[0 for _ in range(m)] for _ in range(n)]
maxSize = 0

# 첫 번째 행과 첫 번째 열은 그대로 dp 배열에 저장
for i in range(n):
    dp[i][0] = pan[i][0]
    maxSize = max(maxSize, dp[i][0])

for j in range(m):
    dp[0][j] = pan[0][j]
    maxSize = max(maxSize, dp[0][j])


# 나머지 칸들을 계산하여 dp 배열에 저장
for i in range(1, n):
    for j in range(1, m):
        if pan[i][j] == 1:
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
            maxSize = max(maxSize, dp[i][j])

    for i in dp:
        print(i)
    print('-------------------------')

print(maxSize **2)  # 가장 큰 정사각형의 넓이 출력


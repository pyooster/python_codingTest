M, N = map(int, input().split())
matrix = []
for _ in range(M):
    row = list(map(int, input().split()))
    matrix.append(row)

# 다이나믹 프로그래밍 배열 초기화
dp = [[-1] * N for _ in range(M)]

# 재귀 함수를 사용하여 가장 큰 정사각형의 한 변의 길이를 계산
def findLargestSquare(x, y):
    if x < 0 or y < 0:
        return 0
    if matrix[x][y] == 0:
        if dp[x][y] == -1:
            top = findLargestSquare(x-1, y)
            left = findLargestSquare(x, y-1)
            topLeft = findLargestSquare(x-1, y-1)
            dp[x][y] = min(top, left, topLeft) + 1
        return dp[x][y]
    return 0

L = 0
for i in range(M):
    for j in range(N):
        if matrix[i][j] == 0:
            L = max(L, findLargestSquare(i, j))

print(L)
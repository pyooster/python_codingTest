import sys

si = sys.stdin.readline

INT_MIN = -sys.maxsize

dirA = [[-1, 0], [0, 1]]
dirB = [[-1, 0], [0, -1]]

n, m = map(int, si().split())
board = [list(map(int, si().split())) for _ in range(n)]

# 전체 배열에 대해 초기화해주고 특정 지점까지 채워주면 된다.
# 초기화 자체를 변곡점에 맞춰 동적으로 범위를 지정해서 해줄 필요가 없다는 의미이다
# 최대 점수를 구하기 때문에 최소로 초기화
# 시작점 부터 변곡점 까지 이동할때 최대 비행 점수
dpA = [[INT_MIN] * m for _ in range(n)]
# 끝점 부터 변곡점 까지 이동할때 최대 비행 점수
dpB = [[INT_MIN] * m for _ in range(n)]

# 기저 조건
dpA[n - 1][0] = board[n - 1][0]

# 변곡점 이전
for i in range(n - 1, -1, -1):
    for j in range(m):
        for k in range(2):
            ni = i + dirA[k][0]
            nj = j + dirA[k][1]
            if 0 <= ni < n and 0 <= nj < m:
                dpA[ni][nj] = max(dpA[ni][nj], dpA[i][j] + board[ni][nj])

# 기저 조건
dpB[n - 1][m - 1] = board[n - 1][m - 1]

# 변곡점 이후
for i in range(n - 1, -1, -1):
    for j in range(m - 1, -1, -1):
        for k in range(2):
            ni = i + dirB[k][0]
            nj = j + dirB[k][1]
            if 0 <= ni < n and 0 <= nj < m:
                dpB[ni][nj] = max(dpB[ni][nj], dpB[i][j] + board[ni][nj])

ans = INT_MIN
for i in range(n):
    for j in range(m):
        ans = max(ans, dpA[i][j] + dpB[i][j])
print(ans)

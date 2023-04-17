# 펠린드롬
import sys
input = sys.stdin.readline

N = int(input())
num = list(input().split())
M = int(input())
dp = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):      # 길이가 1
    dp[i][i] = 1

for i in range(N-1):    # 길이가 2
    if num[i] == num[i+1]:
        dp[i][i+1] = 1

for i in range(2, N):   # 길이가 3이상
    for j in range(N-i):
        # 양 끝이 같고 그사이의 값들이 다 펠린드롬일 경우
        if num[j] == num[j+i] and dp[j+1][j+i-1] == 1:
            dp[j][i+j] = 1

for i in dp:
    print(i)

for i in range(M):
    start, end = map(int, input().split())
    print(dp[start-1][end-1])











def function(a, b):
    temp = num[a:b]
    rev = list(reversed(temp))
    # print(temp)
    # print(rev)
    if temp == rev:
        return 1
    else:
        return 0
# LIS
# 최장 증가 부분 수열의 길이 출력
# dp[i], i번 위치 까지 최장 증가 부분 수열의 길이

import sys

si = sys.stdin.readline

n = int(si())
arr = []

for _ in range(n):
    arr.append(int(si()))

dp = [0] * n


def preprocess():
    for i in range(n):
        dp[i] = -sys.maxsize

    dp[0] = 1


preprocess()

for i in range(1, n):
    dp[i] = 1
    for j in range(0, i):
        if arr[j] < arr[i] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1

len_lis = 0
for i in range(n):
    len_lis = max(len_lis, dp[i])

# print(len_lis)
print(n - len_lis)



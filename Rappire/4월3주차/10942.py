import sys

input = sys.stdin.readline

num = int(input())
arr = list(map(int, input().split()))
dp = [[0 for i in range(num)] for i in range(num)]


#1개, 2개 고려하면 쉽게 풀수 있음
for i in range(num):
    for j in range(num - i):
        if arr[j] == arr[j + i]:
            if j == j + i:
                dp[j][j + i] = 1
            elif j + 1 > j + i - 1:
                dp[j][j + i] = 1
            else:
                dp[j][j + i] = dp[j + 1][j + i - 1]


num = int(input())
for i in range(num):
    S, E = map(int, input().split())
    print(dp[S - 1][E - 1])

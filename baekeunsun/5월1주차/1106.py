# 호텔
import sys

C,N = map(int,input().split())
promotion = [list(map(int,input().split())) for _ in range(N)]

dp = [sys.maxsize for _ in range(C+100)]
dp[0] = 0
 
for value, customer in promotion:
    for i in range(customer,C+100):
        dp[i] = min(dp[i - customer] + value, dp[i]) # i명일 때, 최소비용 갱신
 
print(min(dp[C:]))  # 최소 C명이 되어야 하기 때문

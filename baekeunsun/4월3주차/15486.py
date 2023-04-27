# 퇴사 2
import sys
input = sys.stdin.readline

N = int(input())
dp = list(0 for _ in range(N+1))

for now in range(N):
    T,P = map(int,input().split(' '))
    
    dp[now+1] = max(dp[now+1],dp[now])    
    if now + T < N+1 :
        dp[now+T] = max(dp[now+T],dp[now]+P)

print(dp[-1])

# 영훈이의 색칠공부

N = int(input())
ans = 0

dp = [0] * 100001
dp[0] = 0
dp[1] = 0
dp[2] = 1
fact = 1

for i in range(3, N+1):
    dp[i] = ((i-1) * (dp[i-1]+dp[i-2])) % 1000000007

for i in range(1, N+1):
    fact *= i
    fact = fact % 1000000007

print((fact * dp[N]) % 1000000007)
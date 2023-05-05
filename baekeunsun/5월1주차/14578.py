# 영훈이의 색칠공부
N = int(input())
dp = [0,0,1]
fact = 2
mod = 1000000007

if N > 1 :
    for i in range(3,N+1):
        dp.append(((dp[i-1]+dp[i-2])*(i-1))%mod)
        fact *= i
    print((fact*dp[N])%mod)
    
else :
    print(0)

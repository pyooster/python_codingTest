# 물병

N, K = map(int, input().split())
ans = 0
while bin(N).count('1') > K:
    N += 1
    ans += 1
print(ans)
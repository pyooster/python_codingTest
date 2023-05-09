# 호텔

C, N = map(int, input().split())
dp = [9999999] * 1101
dp[0] = 0
ans = 9999999
arr = []
for i in range(N):
    temp = list(map(int, input().split()))
    arr.append(temp)

for cost, num in arr:                           # 호텔들을 돌면서
    for i in range(num, 1101):                  # 1001로 햇더니 틀림...
        dp[i] = min(dp[i], dp[i-num] + cost)    # 현재고객 수 일때의 최솟 가격
        if i >= C:                              # 고객의 최솟값
            ans = min(ans, dp[i])

print(ans)

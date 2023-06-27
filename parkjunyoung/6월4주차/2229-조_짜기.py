# 조 짜기

N = int(input())

arr = list(map(int, input().split()))
dp = [0] * 1001
# 나이순으로 정렬되어있고 순서를 섞지 않는다
# 앞에서 부터 조를 잘라가면서 탐색

dp[1] = abs(arr[1] - arr[0])

for i in range(1, N):
    for j in range(1, i+1):
        # print(i,j)
        temp_max = max(arr[i-j+1:i+1])
        temp_min = min(arr[i-j+1:i+1])
        dp[i] = max(dp[i], dp[i-j] + temp_max - temp_min)



# print(dp)
print(dp[N-1])
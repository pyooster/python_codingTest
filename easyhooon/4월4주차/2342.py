import sys

si = sys.stdin.readline

INT_MAX = sys.maxsize

arr = list(map(int, si().split()))
arr.pop()
n = len(arr)


# 점프할 때 비용
def get_cost(before, after):
    if before == 0:
        if after == 0:
            return 0
        else:
            return 2
    elif before == after:
        return 1
    elif abs(before - after) == 1 or abs(before - after) == 3:
        return 3
    else:
        return 4


# if n == 0:
#     print(0)
#     exit()

# dp[i][j][k]:= i번째 점프에서 왼발의 위치가 j 이고 오른발의 위치가 k 일때 최소 비용
dp = [[[INT_MAX for _ in range(5)] for _ in range(5)] for _ in range(n + 1)]
dp[-1][0][0] = 0

for i in range(n):
    # l = arr[i], 왼발로 이번 위치 누를 때, 즉 이번에 왼발이 움직일 것
    for r in range(5):  # 왼발이 움직이니 오른발은 고정
        for before in range(5):  # k 는 왼발의 이전 위치.
            cost = get_cost(before, arr[i])  # 왼발이 k에서 arr[i]로 움직일 때 드는 비용
            dp[i][arr[i]][r] = min(dp[i][arr[i]][r], dp[i - 1][before][r] + cost)

    # r = arr[i], 오른발로 이번 위치 누를 때, 즉 이번에 오른발이 움직일 것
    for l in range(5):  # 오른발이 움직이니 왼발은 고정
        for before in range(5):  # k는 오른발의 이전 위치.
            cost = get_cost(before, arr[i])  # 오른발이 k에서 arr[i]로 움직일 때 드는 비용
            dp[i][l][arr[i]] = min(dp[i][l][arr[i]], dp[i - 1][l][before] + cost)

answer = INT_MAX

for l in range(5):
    for r in range(5):
        answer = min(answer, dp[n - 1][l][r])

print(answer)

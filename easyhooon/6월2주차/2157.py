# 여행

import sys

# n 개의 도시 중 m 개 이하의 도시를 지나는 여행을 계획할때 먹게 된느 기내식 점수의 총합이 최대가 되도록
# dp[i][j] := i 번째 도시를 j 개 이하의 도시를 지나 도착했을때 먹은 기내식 점수의 총합
# 동 -> 서로, 도시 번호가 증가하는 순서대로만 이동 가능
# 예제 1 -> 3, 2개의 도시를 지나(3개 이하) 기내식 점수를 10점 얻는게 정답

si = sys.stdin.readline

n, m, k = map(int, si().split())

arr = [[0] * 301 for _ in range(301)]
# i 도시에서 j 도시로 갈때 얻을 수 있는 기내식 점수의 최대
dp = [[-1] * 301 for _ in range(301)]

for _ in range(k):
    a, b, c = map(int, input().split())
    if a > b:
        continue
    arr[a][b] = max(arr[a][b], c)


def solve(idx, cnt):
    # 기저 조건
    if idx != 1 and cnt == 1:
        return -sys.maxsize

    # 기저 조건
    if idx == 1:
        return 0

    # 이미 채운 값이 있는 경우
    if dp[idx][cnt] != -1:
        return dp[idx][cnt]

    # 최댓값을 구하는 것이므로 최솟값으로 초기화
    dp[idx][cnt] = -sys.maxsize

    for i in range(1, idx):
        # 존재하는 경로에 대해서
        if arr[i][idx]:
            dp[idx][cnt] = max(dp[idx][cnt], solve(i, cnt - 1) + arr[i][idx])

    return dp[idx][cnt]


ans = solve(n, m)

print(ans)

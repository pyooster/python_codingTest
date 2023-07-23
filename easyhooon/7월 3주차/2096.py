# 내려가기
# 메모리 초과

import sys

si = sys.stdin.readline

n = int(si())

# 동등한 상황
# 여태 고려한 위치가 같고, 현재 선택하려는 위치가 같으며, 여태까지 고른 숫자들의 합이 같은 경우
# 지금까지 고려한 위치가 같고, 현재 선택하려는 위치가 같다면, 합이 클수록/작을 수록 좋다
# i 번째 줄에서 j 칸을 선택 했을때 여태 까지 얻은 점수의 최대 합
# max_dp = [[0] * 3 for _ in range(n)]
# i 번째 줄에서 j 칸을 선택 했을때 여태 까지 얻은 점수의 최소 합
# min_dp = [[0] * 3 for _ in range(n)]
max_dp = [0] * 3
min_dp = [0] * 3

max_temp = [0] * 3
min_temp = [0] * 3

for i in range(n):
    x, y, z = map(int, si().split())
    for j in range(3):
        if j == 0:
            max_temp[j] = max(max_dp[0], max_dp[1]) + x
            min_temp[j] = min(min_dp[0], min_dp[1]) + x

        elif j == 1:
            max_temp[j] = max(max_dp[0], max_dp[1], max_dp[2]) + y
            min_temp[j] = min(min_dp[0], min_dp[1], min_dp[2]) + y

        elif j == 2:
            max_temp[j] = max(max_dp[1], max_dp[2]) + z
            min_temp[j] = min(min_dp[1], min_dp[2]) + z

    for j in range(3):
        max_dp[j] = max_temp[j]
        min_dp[j] = min_temp[j]

print(max(max_dp), min(min_dp))


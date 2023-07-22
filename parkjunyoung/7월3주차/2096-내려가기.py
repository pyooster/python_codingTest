# 내려가기
import sys
input = sys.stdin.readline
N = int(input())
arr = []
max_dp = [0, 0, 0]
min_dp = [0, 0, 0]
max_temp = [0, 0, 0]
min_temp = [0, 0, 0]

for i in range(N):
    a, b, c = map(int, input().split())

    for j in range(3):
        # 1번위치에서
        if j == 0:
            # 1번 위치 2번 위치 중 최대 최소를 더하면 현재위치의 최대 최소
            max_dp[0] = max(max_temp[j], max_temp[j+1]) + a
            min_dp[0] = min(min_temp[j], min_temp[j+1]) + a
        # 2번 위치에서
        elif j == 1:
            # 1번 2번 3번 중 최대 최소
            max_dp[1] = max(max_temp[j-1], max_temp[j], max_temp[j+1]) + b
            min_dp[1] = min(min_temp[j-1], min_temp[j], min_temp[j+1]) + b
        # 3번 위치에서
        elif j == 2:
            # 2번 3번 중 최대 최소
            max_dp[2] = max(max_temp[j-1], max_temp[j]) + c
            min_dp[2] = min(min_temp[j-1], min_temp[j]) + c
    max_temp = max_dp.copy()
    min_temp = min_dp.copy()
    # print(max_dp)


    # print(min_dp)
print(max(max_dp), min(min_dp))
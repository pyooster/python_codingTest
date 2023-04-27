# 높이의 기준을 찾기 어려움
import sys

si = sys.stdin.readline


def get_rain_amount(heights):
    n = len(heights)
    left_max = [0] * n
    right_max = [0] * n
    cnt = 0

    # 왼쪽에서 오른쪽으로 이동하며 각 위치에서 왼쪽의 최대 높이를 계산
    left_max[0] = heights[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], heights[i])

    # 오른쪽에서 왼쪽으로 이동하며 각 위치에서 오른쪽의 최대 높이를 계산
    right_max[n - 1] = heights[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], heights[i])

    # 현재 위치에서 빗물이 차있는 높이에서 현재 위치의 높이를 빼서 누적 합
    for i in range(n):
        cnt += min(left_max[i], right_max[i]) - heights[i]

    return cnt


h, w = map(int, si().split())
heights = list(map(int, si().split()))

print(get_rain_amount(heights))
# 우체국
# 각 사람들까지의 거리의 합이 '최소'가 되는 위치에 우체국을 세운다.
# 가능한 경우가 여러가지 인 경우 더 작은 위치를 출력하도록 한다.
# 파라매트릭 서치인가
# mid 에 우체국을 세울때 각 사람들까지의 거리의 합이 최소인가? 로 문제를 변형

import sys

si = sys.stdin.readline

INT_MAX = sys.maxsize

n = int(si())

location = [0] * (n + 1)
personnel = [0] * (n + 1)

for i in range(1, n + 1):
    x, a = map(int, si().split())
    location[i] = x
    personnel[i] = a

left = 0
right = 1_000_000_000
min_distance_sum = INT_MAX
answer = 0


def get_distance_sum(mid):
    # 각 사람들로 부터 위치의 합을 구함
    length = 0
    for i in range(1, n + 1):
        length += abs(location[i] - mid) * personnel[i]

    # 더 작은 지점
    return length


# 아 mid 는 결과 값이 아니다..
while left <= right:
    mid = (left + right) // 2
    distance_sum = get_distance_sum(mid)

    if distance_sum <= min_distance_sum:
        # 최소를 구하는 것이기 때문에
        min_distance_sum = distance_sum
        answer = mid
        right = mid - 1
        # print(left, right, mid)
    else:
        left = mid + 1


print(answer)
# 통나무 건너뛰기

# 각 인접한 통나무의 높이 차가 최소가 되도록
# 높이 차의 최댓값으로 난이도가 결정
# 최소 난이도를 출력
# 원형으로 이어지는 구조라 정렬하면 가장 작은 것과 가장 큰게 인접함 -> 최대 난이도를 형성함
# 그리디인가 - 가장 큰거랑 작은게 인접하게 하면 안됨
# 가장 큰거를 가운데에 위치 시키고 왼쪽 오른 쪽 번갈아 놓으면
# 왼쪽에 그 다음으로 큰거 오른쪽에 그 다음로 큰거를 위치시킨다 가정하면 인접한 높이의
# 10, 10, 11, 11, 12, 12, 13
# 10 10 11 12 13 12 11

# 2 4 5 7 9
# 2 5 9 7 4

# 6 6 6 6 6 6 6

import sys

si = sys.stdin.readline

# t 의 범위는 없음
tc = int(si())
# n <= 10,000 -> 2중 포문 가능
# 통나무의 높이 <= 100,000
for _ in range(tc):
    n = int(si())
    arr = list(map(int, si().split()))
    arr.sort()
    max_diff = -sys.maxsize
    for i in range(2, n):
        max_diff = max(max_diff, arr[i] - arr[i - 2])
    print(max_diff)



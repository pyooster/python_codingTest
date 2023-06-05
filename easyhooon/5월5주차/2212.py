# 센서

# 고속도로 위에 n 개의 센서를 설치
# 최대 k 개의 집중국을 설치
# n 개의 센서가 적어도 하나의 집중국과는 통신이 가능해야 함
# 집중국의 유지비 문제로 인해 각 집중국의 수신 가능 영역의 길이의 '합'을 최소화
# 6
# 2
# 1 6 9 3 6 7
# 센서의 좌표가 한 개의 정수로 n 개 주어짐
# 1 3 (6, 6), 7, 9

# 하나의 집중국이 1 ~ 3 = 2
# 다른 하나가 6 ~ 9 = 3
# 5 최소

import sys

si = sys.stdin.readline

# n <= 10000
n = int(si())
# k <= 1000
k = int(si())

nums = list(map(int, si().split()))

nums.sort()

if k >= n:
    print(0)
    exit(0)

dist = []
for i in range(1, n):
    dist.append(nums[i] - nums[i - 1])

dist.sort(reverse=True)
for _ in range(k - 1):
    dist.pop(0)

print(sum(dist))

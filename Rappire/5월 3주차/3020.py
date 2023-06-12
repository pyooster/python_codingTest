import sys
from collections import Counter
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

N, H = map(int, input().split())

up = []
down = []

for i in range(N):
    now = int(input())
    if i % 2 == 1:
        # 종유석
        up.append(now)
    else:
        # 석순
        down.append(now)

up.sort()
down.sort()

upLength = len(up)
downLength = len(down)
countMap = [0 for i in range(H)]

for i in range(H):
    countMap[i] += downLength - bisect_right(down, i)
    countMap[i] += upLength - bisect_left(up, H - i)

count = Counter(countMap)
num = min(count)
print(num, count[num])

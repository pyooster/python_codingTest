# 카드 정렬하기

import sys
import heapq

si = sys.stdin.readline

n = int(si())
pq = []

for _ in range(n):
    num = int(si())
    heapq.heappush(pq, num)

min_sum = 0
while len(pq) > 1:
    num1 = heapq.heappop(pq)
    num2 = heapq.heappop(pq)
    min_sum += num1 + num2

    heapq.heappush(pq, num1 + num2)

print(min_sum)


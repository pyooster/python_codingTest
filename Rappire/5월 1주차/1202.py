import sys
from heapq import heappush, heappop

input = sys.stdin.readline
N, K = map(int, input().split())

jewels = []
for i in range(N):
    jewels.append(list(map(int, input().split())))

knaps = []
for i in range(K):
    knaps.append(int(input()))

knaps.sort()
jewels.sort()
result = 0
jewelsQueue = []
pos = 0
for knap in knaps:
    while pos < len(jewels) and knap >= jewels[pos][0]:
        heappush(jewelsQueue, -jewels[pos][1])
        pos += 1

    if len(jewelsQueue) > 0:
        result -= heappop(jewelsQueue)

print(result)

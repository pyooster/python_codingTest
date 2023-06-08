import sys
from heapq import heappop, heappush

input = sys.stdin.readline
N, M = list(map(int, input().split()))
gift = list(map(int, input().split()))
child = list(map(int, input().split()))
queue = []
for i in gift:
    heappush(queue, -i)

for i in child:
    now = -heappop(queue)
    if now < i:
        print(0)
        sys.exit()
    heappush(queue, -now + i)
print(1)

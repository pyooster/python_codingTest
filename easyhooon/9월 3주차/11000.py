# import sys
# import heapq
# 
# si = sys.stdin.readline
# 
# # n <= 200,000
# n = int(si())
# 
# pq = []
# 
# for _ in range(n):
#     start, end = map(int, si().split())
#     heapq.heappush(pq, (start, end))
# 
# # cnt = 1
# before_end = [0]
# 
# for _ in range(n):
#     start, end = heapq.heappop(pq)
#     for i in range(len(before_end)):
#         if start >= before_end[i]:
#             before_end[i] = end
#             break
#     else:
#         # cnt += 1
#         before_end.append(start)
# 
# # print(before_end)
# # print(cnt)
# print(len(before_end))

import sys
import heapq

si = sys.stdin.readline

n = int(si())

arr = []
for _ in range(n):
    start, end = map(int, si().split())
    arr.append((start, end))

arr.sort(key=lambda x: x[0])

pq = []

for start, end in arr:
    if pq and pq[0] <= start:
        heapq.heappop(pq)
    heapq.heappush(pq, end)

print(len(pq))
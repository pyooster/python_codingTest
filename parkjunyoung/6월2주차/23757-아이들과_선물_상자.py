# 아이들과 선물 상자
import heapq

N, M = map(int, input().split())
box = list(map(int, input().split()))
child = list(map(int, input().split()))
q = []
for i in box:
    heapq.heappush(q, -i)



# print(q)
flag = 1
for i in child:
    temp = heapq.heappop(q)
    if i > -temp:
        flag = 0
        break
    heapq.heappush(q, i + temp)

print(flag)
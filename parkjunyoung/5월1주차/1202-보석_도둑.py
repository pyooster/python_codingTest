# 보석 도둑
import heapq
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
items = []
for i in range(N):
    M, V = map(int, input().split())
    items.append([M, V])
items.sort()

bag = []
for i in range(K):
    C = int(input())
    bag.append(C)
bag.sort()
ans = [0] * K                                # 각 가방의 최대 보석의 크기
temp = []                                    # 가능한 보석담기

for i in range(K):
    while items and bag[i] >= items[0][0]:   # for 문 돌리니 시간초과,,
        w, cost = heapq.heappop(items)       # 우선순위큐로 맨앞의 값을 빼고
        heapq.heappush(temp, (-cost, w))     # 넣어줄때 -로 넣어서 가장 큰 보석이 맨앞에 오도록

    if temp:                                 # 가능한 보석중에
        # print(temp)
        w, cost = heapq.heappop(temp)        # 제일 큰 보석 넣기
        ans[i] = -w                          # 부호 반대로 넣기


print(sum(ans))                              # 합
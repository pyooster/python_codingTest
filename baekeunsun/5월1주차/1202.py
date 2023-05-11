# 보석 도둑
import heapq
import sys

input = sys.stdin.readline

N, K = map(int,input().split()) # 보석개수, 가방개수
gems = [(list(map(int,input().split()))) for _ in range(N)]  # 무게, 가격
bags = [(int(input())) for _ in range(K)]

gems.sort()
bags.sort()
answer = 0
canBuy = [] # 보석의 가격 저장 리스트
 
for bag in bags:
    while gems and gems[0][0] <= bag:
        heapq.heappush(canBuy, -gems[0][1]) # 최대힙
        heapq.heappop(gems)
    if canBuy:
        answer -= heapq.heappop(canBuy)
        
print(answer)

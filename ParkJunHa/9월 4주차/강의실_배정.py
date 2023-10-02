import heapq

n = int(input())
timeline = list(list(map(int, input().split())) for _ in range(n))
timeline.sort()

pq = []
heapq.heappush(pq, timeline[0][1])

for i in range(1, n):
    if timeline[i][0] < pq[0]:
        heapq.heappush(pq, timeline[i][1])
    
    else:
        heapq.heappop(pq)
        heapq.heappush(pq, timeline[i][1])

print(len(pq))
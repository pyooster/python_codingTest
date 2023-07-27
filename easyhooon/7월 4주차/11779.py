# 최소 비용 구하기 2

# 최소 비용
# 최소 비용을 갖는 경로에 포함되어있는 도시의 개수(출발, 도착 도시 포함
# 경로를 방문하는 도시 순서대로 출력

import sys
import heapq

si = sys.stdin.readline


def dijkstra(start, dist, edges):
    pq = []
    heapq.heappush(pq, (0, start))
    dist[start] = 0

    while pq:
        # 현재 가장 가까운 노드와 그 노드까지의 거리
        min_dist, min_idx = heapq.heappop(pq)

        # 현재 노드가 이미 처리된 적이 있다면 무시
        if dist[min_idx] != min_dist:
            continue

        # 현재 노드와 연결된 다른 노드를 확인
        for target_idx, target_dist in edges[min_idx]:
            # 새로운 경로의 거리
            new_dist = dist[min_idx] + target_dist
            # 새 경로의 거리가 기존 경로보다 짧다면
            if dist[target_idx] > new_dist:
                # 경로 길이 갱신
                dist[target_idx] = new_dist
                # 경로 정보 갱신(target_idx 로 가는 최단 경로 상에 바로 직전에 방문한 노드 min_idx)
                path[target_idx] = min_idx
                heapq.heappush(pq, (new_dist, target_idx))

    return dist


n = int(si())
m = int(si())

dist = [sys.maxsize for _ in range(n + 1)]
edges = [[] for _ in range(n + 1)]
path = [0] * (n + 1)

for _ in range(m):
    x, y, w = map(int, si().split())
    edges[x].append((y, w))

# 출발점의 도시번호, 도착점의 도시번호가 주어짐 -> 다익스트라
start, end = map(int, si().split())

dist = dijkstra(start, dist, edges)
print(dist[end])

# 역순으로 경로를 구함
# 도착지 end 에서 시작하여
# 시작점 start 가 나올기 전 까지 path를 따라 움직임
x = end
nodes = []
nodes.append(end)

while x != start:
    x = path[x]
    nodes.append(x)

print(len(nodes))

for node in nodes[::-1]:
    print(node, end = " ")
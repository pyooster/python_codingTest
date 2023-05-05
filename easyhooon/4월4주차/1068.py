# 트리
import sys

si = sys.stdin.readline

n = int(si())
graph = [[] for _ in range(n)]
# 각 노드의 leaf 노드의 개수
leaf = [0] * n
root = 0


# 정점 x의 부모가 parent, subtree(x) 의 leaf 노드의 개수를 구함
# 트리 dp 에서 많이 쓰던 함수
def dfs(x, parent):
    if not graph[x]:
        leaf[x] += 1

    for y in graph[x]:
        if y == parent:
            continue
        dfs(y, x)
        leaf[x] += leaf[y]


# 각 노드의 부모 노드를 저장
parent = list(map(int, si().split()))

for i in range(n):
    # parent 가 -1 이면 루트 노드
    if parent[i] == -1:
        root = i
        continue
    graph[parent[i]].append(i)

# 제거할 노드
erased = int(si())

for i in range(n):
    if erased in graph[i]:
        graph[i].remove(erased)

if root != erased:
    dfs(root, -1)

print(leaf[root])
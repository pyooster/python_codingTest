# 트리의 지름

V = int(input())
# 트리
tree = [[] for _ in range(V+1)]
for i in range(V):
    temp = list(map(int, input().split()))
    # 2칸씩 점프하면서 노드와 거리를 추가
    for j in range(1, len(temp), 2):
        if temp[j] == -1:
            break
        tree[temp[0]].append((temp[j], temp[j+1]))

# 최대 거리를 저장
max_1 = [-1 for _ in range(V + 1)]
# 1번 노드 부터 시작하면서 방문처리하고 거리를 저장
max_1[1] = 0


def dfs(start, tree, max_1):
    for node, dis in tree[start]:
        # 방문하지 않았다면
        if max_1[node] == -1:
            # 거리를 추가
            max_1[node] = max_1[start] + dis
            dfs(node, tree, max_1)

# 1번 노드부터 탐색
dfs(1, tree, max_1)

# 최대 거리와 노드 뽑기
temp = max(max_1)
ans = [temp, max_1.index(temp)]

# 위에서 찾은 노드에서 최대 거리를 다시 탐색
max_2 = [-1 for _ in range(V+1)]
# 방문 처리하고 위의 노드부터 시작
max_2[ans[1]] = 0
dfs(ans[1], tree, max_2)

# 최대 지름
print(max(max_2))
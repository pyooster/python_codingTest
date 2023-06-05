# 양과 늑대

# 갈 수 있는 모든 노드를 찾는 함수
def get_can_go_nodes(parent, prev, graph):
    # 현재 지점이 아닌 모든 이동 가능한 노드
    # 누적해서 더해 주어야함(이 문제 한정으로 0 - 5 - 1 4 - 8 - 3 - 7 이런식으로 움직일 수 있으려면)
    can_go_nodes = [node for node in prev if node != parent]

    for j in range(len(graph)):
        # 현재 지점에서 이동 가능한 간선일 경우
        if graph[parent][j]:
            # 갈 수 있는 노드에 포함 시킴
            can_go_nodes.append(j)

    return can_go_nodes


# 현재 위치(i)를 기준으로 갈 수 있는 곳 가보기 -> DFS
# 갈 수 있는 모든 edges 탐색
# parent: 지금 위치한 노드
# s: 지금까지 모은 양의 수
# w: 지금까지 모은 늑대의 수
def dfs(parent, s, w, prev, graph, info):
    global answer

    can_go_nodes = get_can_go_nodes(parent, prev, graph)

    # 양의 수와 늑대의 수가 같거나, 갈 수 있는 노드가 존재하지 않는 경우
    if s == w or not can_go_nodes:
        # 정답을 갱신
        if answer < s:
            answer = s
        return

    # 갈 수 있는 노드에 대해서
    for node in can_go_nodes:
        # 가려는 노드에 양이 있는 경우
        if info[node] == 0:
            dfs(node, s + 1, w, can_go_nodes, graph, info)

        # 가려는 노드에 늑대가 있는 경우
        else:
            dfs(node, s, w + 1, can_go_nodes, graph, info)


def solution(info, edges):
    global answer

    answer = 1

    graph = [[False] * len(info) for _ in range(len(info))]

    # 간선이 존재하는 경우 True
    for x, y in edges:
        graph[x][y] = True

    # 탐색 시작
    # 0번 노드부터 시작
    # 0번은 무조건 양이므로 양 1마리, 늑대 0마리
    dfs(0, 1, 0, [0], graph, info)

    return answer
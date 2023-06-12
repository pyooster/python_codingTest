# 이진트리를 구성하는 각 노드의 x, y 좌표를 받아서
# 이를 통해서 이진트리를 구성하고,
# 그 이진 트리의 전위 순회, 후위 순회한 결과를 2차원 배열에 순서대로 담아 return
# 좌표를 통해 트리를 구축하는게 어렵다
import sys

sys.setrecursionlimit(10 ** 6)


# 트리 구축
# y 좌표는 같을 수 있지만, x 좌표는 다 다르다.
def add_node(parent, child, tree):
    # 부모 노드보다 x 좌표가 작을 경우, 왼쪽 자식 노드에 들어갈 수 있는지 검사
    if tree[child][0] < tree[parent][0]:
        if tree[parent][1] is None:
            tree[parent][1] = child
        # 이미 자식 노드가 존재한다면
        else:
            # 부모의 왼쪽 자식 노드를 부모로 설정하여 그 부모에 자식 노드가 될 수 있는지 검사(탐색)
            add_node(tree[parent][1], child, tree)

    # 부모 노드보다 x 좌표가 클 경우, 오른쪽 자식 노드에 들어갈 수 있는지 검사
    else:
        if tree[parent][2] is None:
            tree[parent][2] = child
        else:
            add_node(tree[parent][2], child, tree)


# 전위 탐색
# root -> left -> right
def pre_order(node, tree, order):
    # None 이면 존재하지 않으므로 종료
    if node is None:
        return

    order.append(node)
    pre_order(tree[node][1], tree, order)
    pre_order(tree[node][2], tree, order)


# 후위 탐색
# left -> right -> root
def post_order(node, tree, order):
    if node is None:
        return

    post_order(tree[node][1], tree, order)
    post_order(tree[node][2], tree, order)
    order.append(node)


def solution(nodeinfo):
    info = {}
    for idx, node in enumerate(nodeinfo):
        x, y = node
        info[idx + 1] = (x, y)


    # print("info: ", info)

    # 트리의 루트 노드 찾기
    # 각 노드의 위상 관계 찾기 (앞에 있을 수록 루트에 가까움, 왼쪽 자식, 오른쪽 자식 순)
    # 1) y 좌표가 클수록, y 좌표가 같으면 x 좌표가 작을 수록 더 앞선 노드이다.
    nodes = sorted(list(info.keys()), key=lambda x: (-info[x][1], info[x][0]))
    # print("nodes: ", nodes)

    # { node: (node의 x 좌표, left_child, right_child) }
    # y 좌표는 중복이 있지만, x 좌표를 고유값 -> x 좌푤르 통해 각 노드의 위치를 특정
    tree = {node: [info[node][0], None, None] for node in nodes}
    # print("tree: ", tree)

    root = nodes[0]
    for node in nodes[1:]:
        add_node(root, node, tree)

    # print("tree: ", tree)

    pre_order_list = []
    post_order_list = []

    pre_order(root, tree, pre_order_list)
    post_order(root, tree, post_order_list)

    return [pre_order_list, post_order_list]


print(solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]))

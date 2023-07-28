# 이진 검색 트리
import sys

sys.setrecursionlimit(10 ** 6)

si = sys.stdin.readline

# 전위 순위 결과의 순서의 리스트를 통해 이진 탐색 트리를 구성하고
# 그 트리의 후위 순회 결과를 출력

# (루트, 완쪽, 오른쪽)


# 후위 순위
# start: 서브 트리의 시작 인덱스
# end: 서브 트리의 끝 인덱스
def post_order(start, end):
    # 시작 인덱스가 끝 인덱스보다 크면 재귀 종료
    if start > end:
        return

    # 루트 노드의 오른쪽 서브 트리가 시작되는 인덱스
    # 루트 노드보다 큰 값이 나오는 첫번재 인덱스
    division = end + 1
    # 전위 순회 리스트를 순회 하면서
    for i in range(start + 1, end + 1):
        # 루트보다 큰 값을 찾으면
        if pre_order[start] < pre_order[i]:
            # 그 인덱스를 division 으로 설정하고
            division = i
            # 탈출
            break

    # 후위 순위
    # 루트의 왼쪽 서브 트리에 대해 같은 작업을 수행
    post_order(start + 1, division - 1)
    # 루트의 오른쪽 서브트리에 대해 같은 작업을 수행
    post_order(division, end)
    # 모든 자식 노드를 방문한 후에 루트 노드를 출력
    print(pre_order[start])


pre_order = []

for line in sys.stdin:
    pre_order.append(int(line))

# eof (end of file)
# while True:
#     try:
#         pre_order.append(int(si()))
#     except:
#         break

post_order(0, len(pre_order) - 1)

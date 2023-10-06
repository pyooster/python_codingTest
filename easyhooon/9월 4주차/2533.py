# 사회망 서비스
# 얼리어답터가 아닌 사람들은 자신의 모든 친구들이 얼리 어답터일 때만 이 아이디어를 받아들인다.
# 부모 노드가 일반인 -> 자식노드는 전부 얼리어답터여야 함
# -> 자식 노드의 dp 값을 모두 더해줘야 함
# 부모 노드가 얼리어답터일 경우 자식 노드가 얼리어답터이거나, 아닐 경우 둘 중 작은 dp 값을 더해줌
# 0 -> 일반인, 1 -> 얼리어답터
# dp[parent][0] += dp[child][1]
# dp[parent][1] += min(dp[child][0], dp[child][0]
# 1번 노드를 트리의 루트로 설정
import sys

sys.setrecursionlimit(10 ** 6)

si = sys.stdin.readline

n = int(si())
# 필요한 최소 얼리어답터 수
graph = [[] for _ in range(n + 1)]
dp = [[0 for _ in range(2)] for _ in range(10 ** 6 + 1)]
visited = [False] * (10 ** 6 + 1)
answer = 0


def dfs(root):
    visited[root] = True
    # 기저 조건
    dp[root][1] = 1
    # 점화식
    for i in range(len(graph[root])):
        child = graph[root][i]
        if not visited[child]:
            dfs(child)
            dp[root][0] += dp[child][1]
            dp[root][1] += min(dp[child][0], dp[child][1])


for _ in range(n - 1):
    u, v = map(int, si().split())
    graph[u].append(v)
    # 양방향 연결 반드시 필요 
    graph[v].append(u)

# print(graph)

dfs(1)

answer = min(dp[1][0], dp[1][1])
print(answer)

# 치킨 배달
# 맨하탄 거리
# 집의 개수는 2N 개를 넘지 않으며, 적어도 1개는 존재
import sys

si = sys.stdin.readline

# 2 <= n <= 50, 도시의 한변의 길이
# 1 <= m <= 13, 도시에 있는 치킨 집 중 최대 M개를 고름, 나머지는 모두 폐업
# 도시의 치킨 거리가 가장 작게 될지 구하는 프로그램
# 치킨 거리: 집에서 가장 가까운 치킨집 사이의 거리
# 폐업시키지 않을 치킨집을 최대 M개를 골랐을 때, 도시의 치킨 거리의 최솟값
# 최대 M 개를 고르는거면 M개 보다 적게 골라도 되는거 아닌가
# 치킨집이 많을수록 각 집에서의 치킨거리는 줄어들기 때문에 M개를 뽑는게 치킨거리의 합을 최소로 만들 수 있다. 
n, m = map(int, si().split())
graph = [[0] * (n + 1)]
for _ in range(n):
    graph.append([0] + list(map(int, si().split())))
chicken = [(0, 0)]
ans = sys.maxsize
selected = [0]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == 2:
            chicken.append((i, j))


def get_chicken_distance_sum():
    chicken_distance_sum = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i][j] == 1:
                chicken_distance = sys.maxsize
                for k in range(1, m + 1):
                    chicken_distance = min(chicken_distance,
                                           abs(i - chicken[selected[k]][0]) + abs(j - chicken[selected[k]][1]))
                chicken_distance_sum += chicken_distance
    return chicken_distance_sum


# 중복을 허용하지 않음
def dfs(curr_num):
    global ans
    if curr_num == m + 1:
        ans = min(ans, get_chicken_distance_sum())
        return

    for cand in range(1, len(chicken)):
        if selected[curr_num - 1] < cand:
            selected.append(cand)
            dfs(curr_num + 1)
            selected.pop()


dfs(1)
print(ans)

# 트리의 지름
import sys
sys.setrecursionlimit(10**6)

si = sys.stdin.readline

MAX = 100_000

n = int(si())
node = [[] for _ in range(MAX + 1)]
visited = [False] * (MAX + 1)
max_len = 0
max_len_point = 0


def dfs(point, length):
    global max_len, max_len_point

    if visited[point]:
        return

    visited[point] = True
    if max_len < length:
        max_len = length
        max_len_point = point

    for i in range(len(node[point])):
        dfs(node[point][i][0], length + node[point][i][1])


for _ in range(n):
    temp_list = list(map(int, si().split()))[:-1]

    cnt = 0
    parent = temp_list[cnt]

    while True:
        cnt += 1
        child_index = cnt
        cnt += 1
        length_index = cnt
        if len(temp_list) <= cnt:
            break
        child = temp_list[child_index]
        length = temp_list[length_index]

        node[parent].append((child, length))
        # 양방향 연결을 해주지 않는게 빠르다
        # node[child].append((parent, length))


# print(node)

# 가장 멀리 있는 정점(max_len_point) 구하기
dfs(1, 0)

max_len = 0

visited = [False] * (MAX + 1)

# max_len_point 와 가장 멀리 있는 정점과의 거리 구하기
dfs(max_len_point, 0)

print(max_len)

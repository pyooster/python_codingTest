width, height = map(int, input().split())
stack = map(int, input().split())
graph = [[0]* height for _ in range(width)]
res = 0

for i, s in enumerate(stack):
    for j in range(s):
        graph[j][i] = 1

for i in range(width):
    for j in range(height):
        if graph[i][j] == 0:
            graph[i][j] = 9

    for k in range(height):
        if graph[i][k] == 9:
            try:
                w_s, w_e = graph[i][:k].index(1), graph[i][k+1:].index(1)
            except ValueError:
                graph[i][k] = -1

print(sum(graph, []).count(9))

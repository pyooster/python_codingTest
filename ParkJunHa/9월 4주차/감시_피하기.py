import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [list(input().split()) for _ in range(n)]
is_possible = False

# T : 선생님
# S : 학생
# O : 장애물
# X : 빈공간
def obstacle(k=3):
    global is_possible, graph
    if k == 0:
        import pprint
        # pprint.pprint(graph)
        if bfs():
            is_possible = True
        # print("=============================")
        return

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'X':
                graph[i][j] = 'O'
                obstacle(k-1)
                graph[i][j] = 'X'
    


def bfs():
    from copy import deepcopy
    g = deepcopy(graph)
    q = deque()
    for i in range(n):
        for j in range(n):
            if g[i][j] == 'T':
                q.append([i, j])

    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    while q:
        # print(graph)
        # print()
        cx, cy = q.pop()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            while nx in range(n) and ny in range(n):
                if graph[nx][ny] == 'O':
                    break
                if graph[nx][ny] == 'S':
                    return False
                nx, ny = nx + dx[i], ny + dy[i]
                
    return True


obstacle()
print("YES" if is_possible else "NO")
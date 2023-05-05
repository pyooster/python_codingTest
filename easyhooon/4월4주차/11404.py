# 플로이드
import sys

si = sys.stdin.readline
INT_MAX = sys.maxsize


def floyd():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j:
                    graph[i][j] = 0

                elif graph[i][k] and graph[k][j]:
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


n = int(si())
m = int(si())

graph = [[INT_MAX] * 101 for _ in range(101)]

for _ in range(m):
    i, j, price = map(int, si().split())
    # 시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있다.
    graph[i - 1][j - 1] = min(graph[i - 1][j - 1], price)

floyd()

for i in range(n):
    for j in range(n):
        if graph[i][j] == INT_MAX:
            print(0, end=" ")
        else:
            print(graph[i][j], end=" ")
    print()

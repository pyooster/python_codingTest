# 플로이드
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = list([sys.maxsize]*n for _ in range(n))


for i in range(m):
    s, e, value = map(int,input().split(' '))
    graph[s-1][e-1] = min(graph[s-1][e-1],value)
    
for j in range(n):
    graph[j][j] = 0
   

for mid in range(n):
    for start in range(n):
        for end in range(n):
            graph[start][end] = min(graph[start][end], graph[start][mid]+graph[mid][end])

for i in range(n):
    for j in range(n):
        if graph[i][j]==sys.maxsize:
            print(0, end=' ')
        else :
            print(graph[i][j], end=' ')
    print()

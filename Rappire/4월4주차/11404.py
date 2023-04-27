import sys

input = sys.stdin.readline
 
N = int(input())
M = int(input())
inf = 10e7
arr = [[inf for _ in range(N)] for _ in range(N)]

for i in range(N):
    arr[i][i] = 0

for i in range(M):
    start, end, cost = map(int, input().split())
    arr[start - 1][end - 1] = min(cost, arr[start - 1][end - 1])

for i in range(N):
    for a in range(N):
        for b in range(N):
            arr[a][b] = min(arr[a][b], arr[a][i] + arr[i][b])


for i in range(N):
    for j in range(N):
        if arr[i][j] == inf:
            print(0, end=" ")
        else:
            print(arr[i][j], end=" ")
    print()

import sys
from itertools import combinations

input = sys.stdin.readline

N, M = list(map(int, input().split()))
mapArr = [list(map(int, input().split())) for _ in range(N)]
chickens = []
homes = []
maxint = sys.maxsize
answer = maxint

for i in range(N):
    for j in range(N):
        if mapArr[i][j] == 1:
            homes.append([i, j])
        elif mapArr[i][j] == 2:
            chickens.append([i, j])

for chicken in combinations(chickens, M):
    total = 0
    for hx, hy in homes:
        temp = maxint
        for cx, cy in chicken:
            temp = min(temp, abs(hx - cx) + abs(hy - cy))
        total += temp
    answer = min(answer, total)

print(answer)

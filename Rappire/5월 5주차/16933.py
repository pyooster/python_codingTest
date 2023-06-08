import sys

input = sys.stdin.readline
N, M, K = map(int, input().split())
mapArr = []
for _ in range(N):
    mapArr.append(input().split())
print(mapArr)

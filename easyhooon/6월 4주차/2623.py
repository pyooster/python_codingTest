# 음악 프로그램
from collections import deque
import sys

si = sys.stdin.readline

n, m = map(int, si().split())

edges = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

for _ in range(m):
    arr = list(map(int, si().split()))
    arr = arr[1:]
    for i in range(len(arr) - 1):
        edges[arr[i]].append(arr[i + 1])
        indegree[arr[i + 1]] += 1

# print(edges)
# print(indegree)

q = deque()

for i in range(1, n + 1):
    # 진입 차수가 0 이 아니라면
    if not indegree[i]:
        q.append(i)

answer = []

while q:
    x = q.popleft()
    answer.append(x)

    for y in edges[x]:
        indegree[y] -= 1

        # 진입 차수가 0이라면
        if not indegree[y]:
            q.append(y)

if len(answer) == n:
    for elem in answer:
        print(elem)

else:
    print(0)

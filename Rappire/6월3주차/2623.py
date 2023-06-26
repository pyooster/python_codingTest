import sys
from collections import deque

input = sys.stdin.readline

N, M = list(map(int, input().split()))

arr = [[0, []] for _ in range(N + 1)]
que = deque([])

for i in range(M):
    temp = list(map(int, input().split()))
    before = -1
    for i in range(1, temp[0]):
        now = temp[i]
        next = temp[i + 1]
        arr[now][1].append(next)
        arr[next][0] += 1

for i in range(1, N + 1):
    temp = arr[i]
    if temp[0] == 0:
        que.append(i)

answer = []
while que:
    now = que.popleft()
    answer.append(now)
    temp = arr[now][1]
    for i in temp:
        arr[i][0] -= 1
        if arr[i][0] == 0:
            que.append(i)

if len(answer) == N:
    for i in answer:
        print(i)
else:
    print(0)

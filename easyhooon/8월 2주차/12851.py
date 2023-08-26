# 숨박꼭질 2
from collections import deque
import sys

# 방법의 가지수도 출력해야 함

si = sys.stdin.readline
# n 번째 칸을 가장 빠른 시간으로 찾는 방법 m 가지
# 큰 수로 초기화 해놓고
# n 번째 칸 (가장 빠른 시간, 방법 수)
# visited = [[sys.maxsize, 0]] * 100001
visited = [[sys.maxsize, 0] for _ in range(100001)]


def bfs(start):
    q = deque()
    q.append((start, 0))
    visited[start][0] = 0
    visited[start][1] = 1
    while q:
        num, cnt = q.popleft()
        # print(num, cnt)

        if num == k:
            print(visited[num][0])
            print(visited[num][1])
            return

        if (num * 2) <= 100000:
            if cnt + 1 < visited[num * 2][0]:
                visited[num * 2][0] = cnt + 1
                visited[num * 2][1] = 1
                q.append((num * 2, cnt + 1))
            elif cnt + 1 == visited[num * 2][0]:
                visited[num * 2][1] += 1
                q.append((num * 2, cnt + 1))

        if (num + 1) <= 100000:
            if cnt + 1 < visited[num + 1][0]:
                visited[num + 1][0] = cnt + 1
                visited[num + 1][1] = 1
                q.append((num + 1, cnt + 1))
            elif cnt + 1 == visited[num + 1][0]:
                visited[num + 1][1] += 1
                q.append((num + 1, cnt + 1))

        if (num - 1) >= 0:
            if cnt + 1 < visited[num - 1][0]:
                visited[num - 1][0] = cnt + 1
                visited[num - 1][1] = 1
                q.append((num - 1, cnt + 1))
            elif cnt + 1 == visited[num - 1][0]:
                visited[num - 1][1] += 1
                q.append((num - 1, cnt + 1))


n, k = map(int, si().split())
bfs(n)

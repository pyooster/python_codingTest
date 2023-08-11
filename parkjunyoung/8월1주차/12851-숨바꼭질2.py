# 숨바꼭질 2

from collections import deque

N, K = map(int, input().split())
q = deque()
q.append(N)

# 방문처리
visited = [0] * 100001
visited[N] = 1


def bfs(q):
    time = 0
    cnt = 0
    while q:
        x = q.popleft()
        # K에 도착하면 개수 +1 시간을 저장하는데 처음부터 1을 줘서 1을 뺀다
        if x == K:
            cnt += 1
            time = visited[K]-1

        # 2배일 경우
        if 0 <= x*2 < 100001:
            # 방문하지 않았거나 같은 시간안에 도착한곳이라면
            if visited[x*2] == 0 or visited[x*2] == visited[x]+1:
                # 현재위치의 시간을 갱신하고 q 에 추가
                visited[x*2] = visited[x]+1
                q.append(x*2)
        # +1 할 경우
        if 0 <= x+1 < 100001:
            if visited[x+1] == 0 or visited[x+1] == visited[x]+1:
                visited[x+1] = visited[x]+1
                q.append(x+1)
        # -1 할 경우
        if 0 <= x-1 < 100001:
            if visited[x-1] == 0 or visited[x-1] == visited[x]+1:
                visited[x-1] = visited[x]+1
                q.append(x-1)

    return [time, cnt]


ans = []
ans = bfs(q)

for i in ans:
    print(i)
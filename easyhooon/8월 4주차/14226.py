# 이모티콘
import sys
from collections import deque

si = sys.stdin.readline

S = int(si())

# 화면에 이미 이모티콘 1개를 입력했다.
# 복사해서 클립보드에 저장
# 붙혀넣기
# 이모티콘 1개를 삭제

# 클립 보드가 비어있는 상태에는 붙혀넣기 불가능, 일부만 클립보드가 복사할 수 없음, 클립보드에 이모티콘 중 일부를 삭제할 수 없음


# visited[화면의 이모티콘 수][클립보드의 이모티콘 수] = 방문 여부
visited = [[0] * (2002) for _ in range(2002)]


def bfs():
    # 화면 이모티콘 수, 클립보드 이모티콘 수, 시간
    q = deque([(1, 0, 0)])  

    while q:
        s, c, time = q.popleft()

        if s == S:
            return time

        # 화면의 이모티콘을 클립보드에 복사
        if not visited[s][s]:
            visited[s][s] = 1
            q.append((s, s, time + 1))

        # 클립보드의 이모티콘을 화면에 붙여넣기
        # <= 1001 로 두면 범위 1001 x 1001 로 둬도 인덱스 에러가 나지 않는다
        if 0 < c <= S and not visited[s + c][c]:
            visited[s + c][c] = 1
            q.append((s + c, c, time + 1))

        # 화면의 이모티콘을 하나 삭제
        if 0 < s and not visited[s - 1][c]:
            visited[s - 1][c] = 1
            q.append((s - 1, c, time + 1))


print(bfs())

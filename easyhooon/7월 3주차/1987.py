# 알파벳
# 최장거리 -> 다항식의 시간 복잡도로 불가능, 백트래킹을 통한 완전 탐색
import sys

si = sys.stdin.readline

n, m = map(int, si().split())
board = [list(si().strip()) for _ in range(n)]
dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))
ans = 0
visited = [False for _ in range(26)]  # 정답 변수 & 사용한 알파벳 기록 배열


def recursive(x, y, cnt):
    global ans
    ans = max(ans, cnt)
    visited[ord(board[x][y]) - ord('A')] = True

    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and not visited[ord(board[nx][ny]) - ord('A')]:
            recursive(nx, ny, cnt + 1)

    visited[ord(board[x][y]) - ord('A')] = False


recursive(0, 0, 1)

print(ans)
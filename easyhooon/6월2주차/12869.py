# 뮤탈리스크
# 남은 scv 를 모두 파괴하기 위해 공격해야하는 횟수의 최솟값
# 3
# 12 10 4
# 12 - 3, 10 - 9, 4 -1 => 9, 1, 3
# 9 - 9, 1 - 1, 3 - 3  => 0, 0, 0
# scv 는 최대 3마리, 체력이 0 이하가 되면 즉시 파괴
# 다 계산 해보면 되는것 같은데, 체력도 적음
# 문제는 몇번 시행한다고 정해진게 아니라 끝날때까지 하는거라 기존의 n과 m 풀이와는 다르게 가져가야
# 아 물병 문제 처럼
# 3 ^ n

import sys
from collections import deque

sys.setrecursionlimit(10 * 6)

si = sys.stdin.readline

n = int(si())
arr = list(map(int, si().split()))

while len(arr) < 3:
    arr.append(0)

visited = [[[False] * 61 for _ in range(61)] for _ in range(61)]
attacks = [(9, 3, 1), (9, 1, 3), (3, 9, 1), (3, 1, 9), (1, 9, 3), (1, 3, 9)]


def bfs():
    q = deque()
    q.append((arr[0], arr[1], arr[2], 0))
    visited[arr[0]][arr[1]][arr[2]] = True

    while q:
        x, y, z, curr_num = q.popleft()

        if x == 0 and y == 0 and z == 0:
            print(curr_num)
            return

        for attack in attacks:
            nx = x - attack[0]
            ny = y - attack[1]
            nz = z - attack[2]
            if nx < 0:
                nx = 0
            if ny < 0:
                ny = 0
            if nz < 0:
                nz = 0
            if not visited[nx][ny][nz]:
                visited[nx][ny][nz] = True
                q.append((nx, ny, nz, curr_num + 1))


bfs()




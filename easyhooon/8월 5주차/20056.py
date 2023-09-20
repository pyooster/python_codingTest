# 마법사 상어와 파이어볼
import sys
from collections import defaultdict

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

si = sys.stdin.readline

n, m, k = map(int, si().split())
graph = [[0] * n for _ in range(n)]
fireballs = []

# def move():


# def merge():


for i in range(1, m + 1):
    # 위치(r, c), 질량 mi, 속력 s, 방향 d(0~7)
    # r, c, mi, s, d = map(int, si().split())
    fireball = list(map(int, si().split()))
    fireballs.append(fireball)

info = defaultdict(list)
for r, c, m, s, d in fireballs:
    info[(r - 1, c - 1)].append((m, s, d))

for _ in range(k):
    new_info = defaultdict(list)
    # move
    for (x, y), vals in info.items():
        for m, s, d in vals:
            # 격자의 행과 열은 1번부터 N번까지 번호가 매겨져 있고, 1번 행은 N번과 연결되어 있고, 1번 열은 N번 열과 연결되어 있다.
            nx, ny = (x + dx[d] * s) % n, (y + dy[d] * s) % n
            new_info[(nx, ny)].append((m, s, d))

    # merge
    for (x, y), vals in new_info.items():
        if len(vals) > 1:
            total_mass = 0
            for m, _, _ in vals:
                total_mass += m
            total_speed = 0
            for _, s, _ in vals:
                total_speed += s
            directions = []
            for _, _, d in vals:
                directions.append(d % 2)

            is_all_even = True
            is_all_odd = True

            for _, _, d in vals:
                if d % 2 == 0:
                    is_all_odd = False

                else:
                    is_all_even = False

            if is_all_even or is_all_odd:
                new_fireballs = []
                for i in range(4):
                    # 질량이 0 보다 큰 것만 필터링
                    if total_mass // 5 > 0:
                        new_fireballs.append((total_mass // 5, total_speed // len(vals), i * 2))
                new_info[(x, y)] = new_fireballs

            else:
                new_fireballs = []
                for i in range(4):
                    if total_mass // 5 > 0:
                        new_fireballs.append((total_mass // 5, total_speed // len(vals), i * 2 + 1))
                new_info[(x, y)] = new_fireballs

    info = new_info

result = 0
for (x, y), vals in info.items():
    for m, _, _ in vals:
        result += m

print(result)

# 체스판 다시 칠하기2

import sys

si = sys.stdin.readline

# n, m <= 2000 -> 판의 최대 칸 수 400만
n, m, k = map(int, si().split())

board = [list(si().strip()) for _ in range(n)]


# k x k 정사각형을 만든다
# 다시 칠해야 하는 칸의 개수를 센다
# 최소 개수를 갱신한다 -> 시간 초과

# 다시 칠해야 하는 칸의 누적합을 먼저 구하고
# k x k 정사각형을 순회하며 최소 개수를 갱신한다.


def get_min_repaint_count(color):
    prefix_sum = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n):
        for j in range(m):
            repaint_count = 0
            if (i + j) % 2 == 0:
                if board[i][j] != color:
                    repaint_count = 1
            else:
                if board[i][j] == color:
                    repaint_count = 1

            prefix_sum[i + 1][j + 1] = prefix_sum[i][j + 1] + prefix_sum[i + 1][j] - prefix_sum[i][j] + repaint_count

    min_repaint_count = sys.maxsize

    for i in range(1, n - k + 2):
        for j in range(1, m - k + 2):
            min_repaint_count = min(min_repaint_count,
                                    prefix_sum[i + k - 1][j + k - 1] - prefix_sum[i + k - 1][j - 1] - prefix_sum[i - 1][
                                        j + k - 1] + prefix_sum[i - 1][j - 1])

    return min_repaint_count


print(min(get_min_repaint_count('B'), get_min_repaint_count('W')))

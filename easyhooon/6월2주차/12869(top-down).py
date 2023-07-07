# 뮤탈리스크 (top-down dp)

import sys

sys.setrecursionlimit(10**6)
si = sys.stdin.readline

n = int(si())
scv = list(map(int, si().split()))

while len(scv) < 3:
    scv.append(0)

scv.sort(reverse=True)

dp = [[[0] * 61 for _ in range(61)] for _ in range(61)]


def solve(i, j, k):
    if i < 0:
        return solve(0, j, k)

    if j < 0:
        return solve(i, 0, k)

    if k < 0:
        return solve(i, j, 0)

    if i == 0 and j == 0 and k == 0:
        return 0

    if dp[i][j][k]:
        return dp[i][j][k]

    ret = sys.maxsize
    ret = min(ret, solve(i - 9, j - 3, k - 1) + 1)
    ret = min(ret, solve(i - 9, j - 1, k - 3) + 1)
    ret = min(ret, solve(i - 1, j - 9, k - 3) + 1)
    ret = min(ret, solve(i - 1, j - 3, k - 9) + 1)
    ret = min(ret, solve(i - 3, j - 9, k - 1) + 1)
    ret = min(ret, solve(i - 3, j - 1, k - 9) + 1)

    dp[i][j][k] = ret
    return ret


print(solve(scv[0], scv[1], scv[2]))

# 뮤탈리스크

from itertools import permutations

N = int(input())
scv = [0, 0, 0]
hp = list(map(int, input().split()))
for i in range(N):
    scv[i] = hp[i]

dp = [[[0 for _ in range(61)] for _ in range(61)] for _ in range(61)]
dp[scv[0]][scv[1]][scv[2]] = 1
mutal = [9, 3, 1]
mutals = list(permutations([9, 3, 1]))
# print(mutals)
# print(dp)
for i in range(60, -1, -1):
    for j in range(60, -1, -1):
        for k in range(60, -1, -1):
            if dp[i][j][k] > 0:
                for a1, a2, a3 in mutals:
                    I = i - a1
                    J = j - a2
                    K = k - a3
                    if i-a1 < 0:
                        I = 0
                    if j-a2 < 0:
                        J = 0
                    if k-a3 < 0:
                        K = 0
                    if dp[I][J][K] == 0 or dp[I][J][K] > dp[i][j][k]+1:
                        dp[I][J][K] = dp[i][j][k]+1

print(dp[0][0][0]-1)


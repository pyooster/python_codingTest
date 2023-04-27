# Dance Dance Revolution
import sys
sys.setrecursionlimit(10**6)
 
def move(a, b):
    if a == b:
        return 1
    if a == 0:
        return 2
    if abs(b-a)%2 == 0:
        return 4
    return 3
 
def solve(n, l, r):
    global dp
    if n >= len(game)-1:
        return 0
 
    if dp[n][l][r] != -1:
        return dp[n][l][r]
    left = solve(n+1, game[n],r) + move(l, game[n])
    right = solve(n+1, l, game[n]) + move(r, game[n])
 
    dp[n][l][r] = min(left, right)
    return dp[n][l][r]
 
game = list(map(int, input().split()))
dp = [[[-1]*5 for _ in range(5)] for _ in range(100000)]
 
print(solve(0, 0, 0))

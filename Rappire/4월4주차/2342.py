import sys

 
def cost(pos, last):
    if last == 0:
        return 2
    calc = abs(pos - last)
    if calc == 2:
        return 4
    elif calc == 0:
        return 1
    return 3


# 1=>3
# 2=>4
# 처음에는 2
# 차이가 2나면 4, 아니면 3, 같은거 1
input = sys.stdin.readline
arr = list(map(int, input().split()))
arr.pop()
maxNum = int(10e8)
lastdp = [[maxNum for _ in range(5)] for _ in range(5)]
dp = [[maxNum for _ in range(5)] for _ in range(5)]
lastdp[0][0] = 0

for now in arr:
    for left in range(5):
        for right in range(5):
            dp[now][right] = min(dp[now][right], lastdp[left][right] + cost(now, left))
            dp[left][now] = min(dp[left][now], lastdp[left][right] + cost(now, right))

    lastdp, dp = dp, lastdp
    for i in range(5):
        for j in range(5):
            dp[i][j] = maxNum

minnum = maxNum
for line in lastdp:
    minnum = min(min(line), minnum)
print(minnum)

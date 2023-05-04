# Dance Dance Revolution

cmd = list(map(int, input().split()))

# 왼발 오른발에 따른 패턴 5 * 5
# 전체 100000

dp = [[[999999 for _ in range(5)] for _ in range(5)] for _ in range(100001)]
# 초기값
dp[0][0][0] = 0


# 힘 계산
def power(x, y):
    if x == y:                                # 현재랑 같다면
        return 1
    elif x == 0:                              # 현재가 0이면 어딜가도 2
        return 2
    elif abs(x - y) == 1 or abs(x - y) == 3:  # 차이가 1이나 3이면
        return 3
    else:                                     # 나머지 4
        return 4


for i in range(1, len(cmd)):
    for r in range(5):
        for l in range(5):
            temp1 = power(r, cmd[i-1])
            temp2 = power(l, cmd[i-1])
            dp[i][cmd[i-1]][l] = min(dp[i][cmd[i-1]][l], dp[i-1][r][l] + temp1)
            dp[i][r][cmd[i-1]] = min(dp[i][r][cmd[i-1]], dp[i-1][r][l] + temp2)

# for i in range(len(cmd)):
#     for j in dp[i]:
#         print(j)

hap = 999999
for i in range(5):
    for j in range(5):
        hap = min(hap, dp[len(cmd)-1][i][j])

print(hap)
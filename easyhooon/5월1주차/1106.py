# 호텔
# 돈에 정수배 만큼을 투자할 수 있다.
# -> 동일한 보석을 여러개 고르는 것을 허용
# 고객을 적어도 C 명 늘리기 위해 형택이가 투자해야 하는 돈의 '최솟값'
# 돈, 즉 무게의 최솟값을 구하는 문제
# -> 무게의 제한이 문제에 존재하지 않는다.
# i 원으로 얻을 수 있는 고객이 j 명일 때, C명을 늘릴 수 있는 가장 작은 i원 를 구하는 문제
# C, 늘리고자 하는 고객의 숫자 <= 1000
# N, 도시의 개수(종류) <= 20 <- 숫자가 유의미하게 작다. 중요 포인트
# dp[i] := i 만큼 비용을 사용했을 때, 얻을 수 있는 고객의 최대값
# 최대 비용
# C가 1000명이고, 도시를 홍보할 때 필요한 비용이 100원, 이때 얻을 수 있는 고객이 1명인 경우
# -> 100 * 1000 -> 100,000

# 12 2
# 3 5
# 1 1
# (6, 10) + (2, 2)

# 10 3
# 3 1
# 2 2
# 1 3
# (2, 6) + (4, 4)


import sys

si = sys.stdin.readline

INT_MIN = -sys.maxsize


# c <= 1000
# n <= 20
c, n = map(int, si().split())

weight = [0] * (n + 1)
value = [0] * (n + 1)

for i in range(1, n + 1):
    w, v = map(int, si().split())
    weight[i] = w
    value[i] = v

# dp = [INT_MIN] * (c + 1)
dp = [INT_MIN] * 100001
dp[0] = 0

# 무게를 i 만큼 썼을때 얻을 수 있는 가치의 최대 값을 구할 때 사용하는 방법
# 무게의 범위 <= 100,000
for i in range(1, 100001):
    for j in range(1, n + 1):
        if weight[j] > i:
            dp[i] = max(dp[i], dp[i - 1])
        else:
            dp[i] = max(dp[i], dp[i - weight[j]] + value[j])


# print(dp)
# print(c)

for i in range(1, 100001):
    # print(dp[i])
    if dp[i] >= c:
        print(i)
        exit(0)


# 퇴사2
import sys

# 계단 오르기 문제의 역방향

si = sys.stdin.readline
INT_MIN = -sys.maxsize

n = int(si())

t = [0] * n
p = [0] * n

# 문제 이해 1일째 상담이 3일 걸리면 1일, 2일, 3일까지 상담하고 4일째부터는 다시 상담이 가능하다
# dp[i]:= i번째 날 부터 상담을 진행하였을 때 얻을 수 있는 최대 금액
dp = [0] * (n + 1)

for i in range(n):
    a, b = map(int, si().split())
    t[i] = a
    p[i] = b

# 기저 조건
# 최대 금액을 구하는 문제이므로 -INT_MIN 값으로 dp 배열을 초기화
for i in range(n):
    dp[i] = INT_MIN

dp[n] = 0

# for문 거꾸로 순회 하는 방법도 생각해봐야.
for i in range(n - 1, -1, -1):
    # 상담 종료일이 마지막 날 이후일 경우
    if i + t[i] > n:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], p[i] + dp[i + t[i]])

# print(dp)

# 구하는 값: 첫날 부터 상담을 시작했을 때 얻을 수 있는 최대 금액
print(dp[0])

# 퇴사2

N = int(input())                                # N 입력
day = []                                        # 날
money = []                                      # 수익
dp = [0] * (1500000 + 50)                       # dp 1500000 + 50

for i in range(N):                              # N 만큼 반복
    t, p = map(int, input().split())            # 상담일이랑 값
    day.append(t)                               # 추가
    money.append(p)                             # 추가
# print(day)
# print(money)

for i in range(N):                              # N 만큼 반복
    if dp[i] > dp[i + 1]:                       # 다음날 값보다 현재 수익이 크다면
        dp[i + 1] = dp[i]                       # 위치 바꾸기
    if dp[i + day[i]] < dp[i] + money[i]:       # 현재수익과 i일 뒤의 수익 비교
        dp[i + day[i]] = dp[i] + money[i]       # 큰걸로 갱신
    # print(dp)

print(dp[N])
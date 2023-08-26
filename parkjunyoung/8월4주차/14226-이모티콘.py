# 이모티콘

from collections import deque

S = int(input())


# [화면, 클립보드]
dp = [[-1 for _ in range(1001)] for _ in range(1001)]
# 초기값 1초
dp[1][0] = 0

q = deque()
q.append((1, 0))
while q:
    desktop, clipboard = q.popleft()
    # 1
    if dp[desktop][desktop] == -1:
        dp[desktop][desktop] = dp[desktop][clipboard] + 1
        q.append((desktop, desktop))

    # 2
    if 1 < desktop+clipboard < 1001 and dp[desktop+clipboard][clipboard] == -1:
        dp[desktop+clipboard][clipboard] = dp[desktop][clipboard] + 1
        q.append((desktop+clipboard, clipboard))

    # 3
    if 1 < desktop-1 and dp[desktop-1][clipboard] == -1:
        dp[desktop-1][clipboard] = dp[desktop][clipboard] + 1
        q.append((desktop-1, clipboard))

# print(dp[S])
ans = 9999
for i in dp[S]:
    if i != -1:
        ans = min(ans, i)

print(ans)
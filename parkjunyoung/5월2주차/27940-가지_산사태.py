# 가지 산사태
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
farm = [0] * N
flag = 0
ans = []
for i in range(M):
    t, r = map(int, input().split())
    farm[0] += r     # 어차피 1층에는 계속 쌓일 수 밖에 없다....
    if farm[0] > K:
        ans.append(i+1)
        ans.append(1)
        break

if ans:
    print(*ans)
else:
    print(-1)

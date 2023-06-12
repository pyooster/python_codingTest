# 행복 유치원

N, K = map(int, input().split())
arr = list(map(int, input().split()))

cha = []
for i in range(1, N):
    cha.append(arr[i]-arr[i-1])

cha.sort()
# print(cha)

ans = 0
for i in range(N-K):
    ans += cha[i]

print(ans)
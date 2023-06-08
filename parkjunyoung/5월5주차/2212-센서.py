# 센서

N = int(input())
K = int(input())
arr = list(map(int, input().split()))
arr.sort()

cha = []
for i in range(1, N):
    cha.append(arr[i]-arr[i-1])

cha.sort()

ans = 0
for i in range(N-K):
    ans += cha[i]

print(ans)
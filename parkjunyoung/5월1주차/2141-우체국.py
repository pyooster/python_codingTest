# 우체국
import sys
input = sys.stdin.readline
N = int(input())
hap = 0
arr = []
for i in range(N):
    X, A = map(int, input().split())
    arr.append([X, A])
    hap += A
arr.sort()                  # 마을의 위치 순으로 정렬

temp = 0
ans = 0

for i in range(N):
    temp += arr[i][1]       # 마을 주민수 +
    if temp >= (hap/2):     # 전체 주민의 절반 이상일때
        ans = arr[i][0]     # 현재 마을의 위치 저장
        break

print(ans)

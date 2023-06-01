import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    arr.append(int(input()))

arr.sort(reverse=True)
arr = deque(arr)

ans = 0

for i in range(len(arr)%3):
    ans += arr.pop()

cnt = 0
for a in arr:
    if cnt == 2:
        cnt = 0
        continue
    cnt += 1
    ans += a
    
print(ans)
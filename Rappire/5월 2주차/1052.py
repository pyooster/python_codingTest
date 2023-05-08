import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

arr = deque([])
sum = N
size = 1
while N > 0 and sum > K:
    if N % 2 != 0:
        arr.append(size)
        sum += 1
    sum = sum - N + N // 2
    N //= 2
    size *= 2

arr.append(size)
answer = 0

pos = 0
while sum > K and len(arr) > 2:
    sum -= 1
    answer += arr[pos + 1] - arr[pos]
    arr.popleft()
    arr[0] = arr[0] * 2
print(answer)

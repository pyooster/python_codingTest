import sys

input = sys.stdin.readline

N = int(input())

arr = []
for i in range(N):
    arr.append(int(input()))

arr.sort(reverse=True)

answer = 0

for i, price in enumerate(arr):
    if i % 3 != 2:
        answer += price

print(answer)

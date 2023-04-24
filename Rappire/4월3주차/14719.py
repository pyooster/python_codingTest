import sys

input = sys.stdin.readline
H, W = map(int, input().split())
arr = list(map(int, input().split()))

leftMax = -1
count = 0
sumNum = 0
pos = 0
answer = 0

for i, height in enumerate(arr):
    if leftMax <= height:
        answer += count * leftMax - sumNum
        leftMax = height
        count = 0
        sumNum = 0
        pos = i
    else:
        count += 1
        sumNum += height

if pos < W - 1:
    leftMax = -1
    count = 0
    sumNum = 0
    for i in range(W - 1, pos - 1, -1):
        height = arr[i]
        if leftMax <= height:
            answer += count * leftMax - sumNum
            leftMax = height
            count = 0
            sumNum = 0
        else:
            count += 1
            sumNum += height

print(answer)

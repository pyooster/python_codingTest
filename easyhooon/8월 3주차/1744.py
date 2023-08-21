# 수 묶기
import sys

si = sys.stdin.readline

n = int(si())

# arr = []
# arr.sort()
# print(arr)

positive_num = []
negative_num = []
zero = 0
answer = 0

for _ in range(n):
    num = int(si())
    if num > 1:
        positive_num.append(num)
    elif num == 1:
        answer += 1
    elif num == 0:
        zero += 1
    else:
        negative_num.append(num)

positive_num.sort(reverse=True)
negative_num.sort()

while len(positive_num) > 1:
    answer += positive_num.pop(0) * positive_num.pop(0)

if positive_num:
    answer += positive_num[0]

while len(negative_num) > 1:
    answer += negative_num.pop(0) * negative_num.pop(0)

if negative_num and zero > 0:
    negative_num.pop()

if negative_num:
    answer += negative_num[0]

print(answer)

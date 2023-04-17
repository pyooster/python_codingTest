import sys

input = sys.stdin.readline

num = int(input())
arr = list(map(int, input().split()))

if num == 1:
    print(sum(arr) - max(arr))
    sys.exit()

min_1 = min(arr)

# 양쪽 면중 하나가 선택되니, 작은것 선택!
checklist_2 = [
    [0, 1],
    [0, 2],
    [0, 3],
    [0, 4],
    [1, 2],
    [2, 4],
    [4, 3],
    [3, 1],
    [5, 1],
    [5, 2],
    [5, 3],
    [5, 4],
]
checklist_3 = [
    [0, 1, 2],
    [0, 2, 4],
    [0, 4, 3],
    [0, 3, 1],
    [5, 1, 2],
    [5, 2, 4],
    [5, 4, 3],
    [5, 3, 1],
]
min_2 = 1000
for i, j in checklist_2:
    if min_2 > arr[i] + arr[j]:
        min_2 = arr[i] + arr[j]
min_3 = 1000
for i, j, k in checklist_3:
    if min_3 > arr[i] + arr[j] + arr[k]:
        min_3 = arr[i] + arr[j] + arr[k]
total_num = num * num * num
min_2_num = 8 * num - 12
min_3_num = 4
min_1_num = 5 * num * num - 16 * num + 12
num_sum = min_1_num * min_1 + min_2_num * min_2 + min_3_num * min_3
print(num_sum)

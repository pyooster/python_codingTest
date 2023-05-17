# 2 + 1 세일
# 최소 비용으로 유제품을 구입할 수 있도록
# 4
# 3
# 2
# 3
# 2
# (3, 3, 2), (2) -> 8

# 6
# 6
# 4
# 5
# 5
# 5
# 5
# (6, 5, 5), (5, 5, 4) -> 21


import sys

si = sys.stdin.readline

n = int(si())
arr = []

for _ in range(n):
    arr.append(int(si()))

arr.sort(reverse=True)
# print(arr)
arr.insert(0, 0)

total_sum = sum(arr)
subtract_sum = 0

for i in range(1, n + 1):
    if i % 3 == 0:
        subtract_sum += arr[i]

print(total_sum - subtract_sum)
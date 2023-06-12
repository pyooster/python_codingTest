# 아이들과 선물 상자

import sys
import heapq

si = sys.stdin.readline

# n <= 100,000
# m <= 100,000

# 4 3 2 1
# 1번 아이 -> 4 고름 3 -> 가능 1 3 2 1
# 2번 아이 -> 3 고름 1 -> 가능 1 2 2 1
# 3번 아이 -> 2 고름 2 -> 가능 1 0 2 1
# 4번 아이 -> 2 고름 1 -> 가능 1 0 1 1
# 가능

# 4 3
# 1번 아이 -> 4 고름 3 -> 가능 1 3 2 1
# 2번 아이 -> 3 고름 5 -> 불가능
# 불가능 -> -1 이 아니라 0 출력

n, m = map(int, si().split())
presents = list(map(int, si().split()))
children = list(map(int, si().split()))

pq = []

for i in range(len(presents)):
    heapq.heappush(pq, -presents[i])


for child in children:
    present = -heapq.heappop(pq)
    if child <= present:
        present -= child
        # 다시 넣어줄때도 - 붙혀서 넣어줘야지..
        heapq.heappush(pq, -present)

    else:
        print(0)
        exit(0)

print(1)
# 개똥 벌래
import sys
import bisect

si = sys.stdin.readline

INT_MAX = sys.maxsize

n, h = map(int, si().split())
top = []
bottom = []
result = INT_MAX
result_cnt = 0

for i in range(n // 2):
    top.append(int(si()))
    bottom.append(int(si()))

top.sort()
bottom.sort()

for i in range(1, h + 1):
    # 충돌하지 않는 장애물 수를 구함
    # 정렬된 순서를 유지하며 i 를 top에 삽입할 때, 가장 왼쪽 인덱스
    lower_bound = bisect.bisect_left(top, i)
    # 정렬된 순서를 유지하며 h-i 를 bottom에 삽입할 때, 가장 오른쪽 인덱스 반환
    upper_bound = bisect.bisect_right(bottom, h - i)
    # 전체에서 장애물 중에서 충돌 하지 않을 장애물 수를 빼서 충돌할 장애물 수를 구함
    cnt = n - (lower_bound + upper_bound)

    if result == cnt:
        result_cnt += 1
    elif result > cnt:
        result = cnt
        result_cnt = 1

print(result, result_cnt)

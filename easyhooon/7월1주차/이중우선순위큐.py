import heapq

def solution(operations):
    min_pq = []
    max_pq = []

    for op in operations:
        if op.startswith('I'):
            num = int(op.split(' ')[1])
            heapq.heappush(max_pq, -num)
            heapq.heappush(min_pq, num)

        elif op.startswith('D'):
            # "-1" 이거 int 씌우면 -1 되나 -> 됨
            num = int(op.split(' ')[1])
            # 최댓값 삭제
            if num == 1:
                if max_pq:
                    max_value = heapq.heappop(max_pq)
                    min_pq.remove(-max_value)

            # 최솟값 삭제
            else:
                if min_pq:
                    min_value = heapq.heappop(min_pq)
                    max_pq.remove(-min_value)
        # print(max_pq)
        # print(min_pq)
        # print()

    if max_pq and min_pq:
        answer = [-max_pq[0], min_pq[0]]

    else:
        answer = [0, 0]

    return answer

# print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
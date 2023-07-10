# 이중우선순위큐


import heapq


def heapsort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, value)
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result


def heapsort_r(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, -value)
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result


def solution(operations):
    answer = []
    for i in operations:
        a, b = i.split()
        # I일 경우 숫자 삽입
        if a == "I":
            answer.append(int(b))
        # D일 경우
        elif a == "D":
            # 1이면 최댓값을 삭제
            if b == "1":
                # 값이 있을경우만
                if answer:
                    # 최댓값을 찾기위해 reverse 로 우선순위 큐를 정렬
                    answer = heapsort_r(answer)
                    # 맨앞이 최댓값이니까 삭제
                    heapq.heappop(answer)
            # -1이면 최솟값을 삭제
            elif b == "-1":
                # 값이 있으면
                if answer:
                    # 최솟값을 찾기위해 우선순위 큐 정렬
                    answer = heapsort(answer)
                    # 최솟값 삭제
                    heapq.heappop(answer)

    # 다시 최대값으로 정렬
    answer = heapsort_r(answer)
    if answer:
        # [최댓값 최솟값]
        return [answer[0], answer[-1]]
    else:
        return [0, 0]


print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))
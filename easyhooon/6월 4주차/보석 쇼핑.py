# 진열대의 특정 범위의 보석을 모두 구매하되,
# 진열된 모든 종류의 보석을 적어도 1개 이상 포함하는 가장 짧은 구간을 찾아서 구매
# 3 부터 7 -> 모든 종류 보석 적어도 1개씩 포함
# 슬라이딩 윈도우인가
# 그런데 윈도우의 크기가 정해지지 않았음 그러면 슬라이딩 윈도우를 사용해서 문제를 풀 수 없음
# 그러면 투포인터네
import sys

jew_type = {}


# 보석의 종류가 최대 10만개여서 10만 x 10만이 될 수 있음
def is_possible(m, unique_cnt):
    # flag = True
    # for key in jew_type.keys():
    #     if jew_type[key] < 1:
    #         flag = False
    #         return flag
    #
    return m == unique_cnt


def solution(gems):
    # 진열대(배열)의 길이 List<String>
    n = len(gems)
    # 보석의 종류의 개수
    m = len(set(gems))
    # 현재 유니크한 보석의 개수
    unique_cnt = 0
    answer = []
    min_len_answer = sys.maxsize
    min_L = 0
    min_R = 0
    # 보석의 종류
    for jew in set(gems):
        jew_type[jew] = jew_type.get(jew, 0)

    R = -1
    for L in range(0, n):
        if L >= 1:
            jew_type[gems[L - 1]] -= 1
            if jew_type[gems[L - 1]] == 0:
                unique_cnt -= 1

        while R + 1 < n and not is_possible(m, unique_cnt):
            R += 1
            jew_type[gems[R]] += 1
            if jew_type[gems[R]] == 1:
                unique_cnt += 1

        if is_possible(m, unique_cnt):
            # print(L, R)
            # print(jew_type)

            len_answer = R - L + 1
            if len_answer < min_len_answer:
                min_len_answer = len_answer
                min_L = L + 1  # 인덱스
                min_R = R + 1

    answer = []
    answer.append(min_L)
    answer.append(min_R)

    return answer
# 진열대의 특정 범위의 보석을 모두 구매하되,
# 진열된 모든 종류의 보석을 적어도 1개 이상 포함하는 가장 짧은 구간을 찾아서 구매
# 3 부터 7 -> 모든 종류 보석 적어도 1개씩 포함
# 슬라이딩 윈도우인가
# 그런데 윈도우의 크기가 정해지지 않았음 그럼 아닐수도
# 그러면 투포인터네
import sys

jew_type = {}


def is_possible():
    flag = True
    for key in jew_type.keys():
        if jew_type[key] < 1:
            flag = False
            return flag

    return flag


def solution(gems):
    # 진열대(배열)의 길이 List<String>
    n = len(gems)
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

        while R + 1 < n - 1 or not is_possible():
            R += 1
            print(R)
            jew_type[gems[R]] += 1

        print(L, R)
        print(jew_type)

        len_answer = R - L + 1
        if len_answer < min_len_answer:
            min_len_answer = len_answer
            min_L = L
            min_R = R

    answer = []
    answer.append(min_L)
    answer.append(min_R)

    return answer

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
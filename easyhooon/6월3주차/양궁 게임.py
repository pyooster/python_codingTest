from collections import defaultdict


# 라이언이 어피치를 가장 큰 점수 차이로 이기기 위해서 n 발의 화살을 어떤 과녁 점수에 맞혀야 하는지를 구하려고 함
# dp 같은디
# 어피치보다 같은 점수의 과녁을 하나만 더 맞추면 그 점수를 가져갈 수 있다.
# 시간 10초

def solution(n, info):
    cases = []
    combinations = []

    # 중복 조합
    def dfs(curr_num, start):
        if curr_num == n:
            cases.append(combinations[:])
            return

        for i in range(start, 11):
            combinations.append(i)
            dfs(curr_num + 1, i)
            combinations.pop()

    dfs(0, 0)
    # print(cases)

    cands = []
    win_dict = defaultdict(list)

    # 승패 판단
    def compare(ryan, apeach):
        ryan_score = 0
        apeach_score = 0

        for i in range(11):  # 점수 계산
            if apeach[i] >= ryan[i]:
                if apeach[i] == 0:
                    continue
                apeach_score += 10 - i
            else:
                ryan_score += 10 - i

        # 라이언이 이겼으면
        if ryan_score > apeach_score:
            # win_dict에 {점수 차 : [라이언 결과들]} 형태로 같은 점수 차를 갖는 라이언 결과들을 모음
            win_dict[ryan_score - apeach_score].append(ryan)

    # 중복조합을 이용하여 라이언을 쏠 수 있는 모든 경우의 수를 구함
    for case in cases:
        ryan = [0] * 11
        for i in case:
            ryan[i] += 1
        cands.append(ryan)

    # 이긴 것만 win_dict에 기록
    for cand in cands:
        compare(cand, info)

    # 한번도 이길 수 없다면
    if not win_dict:
        return [-1]

    # 점수 차가 가장 큰 라이언 결과들
    target = win_dict[max(win_dict.keys())]
    # print(target)
    # 가장 큰 점수 차이로 이기는 경우 중에서 가장 낮은 점수를 가장 많이 맞힌 케이스를 출력
    target.sort(key=lambda x: tuple([-x[i] for i in range(10, -1, -1)]))

    return target[0]

# print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))
# print(solution(10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]))

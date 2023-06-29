# 양궁 대회


def solution(n, info):
    def func(n, lion, idx):
        nonlocal cha, answer  # nonlocal 지역변수 전역변수에 따라 다르다는 걸 처음봄

        # 화살을 다 쐈을때
        if idx > 10:
            if n > 0:
                lion[10] += n  # 0점에 다 추가
            # 점수 계산
            score_apeach = 0
            score_lion = 0
            for idx in range(0, 11):
                if lion[idx] > info[idx]:
                    score_lion += 10 - idx
                elif info[idx]:
                    score_apeach += 10 - idx

            # 차이의 최대값을 저장하고 화살을 저장
            if cha < score_lion - score_apeach:
                cha = score_lion - score_apeach
                answer = lion[:]


            # 차이가 같으면 가장 낮은 점수를 더 많이 맞힌 경우를 저장
            elif cha == score_lion - score_apeach:
                # 0점부터 탐색하면서 더 낮은게 있으면 갱신해주기
                for i in range(10, -1, -1):
                    if answer[i] < lion[i]:
                        answer = lion[:]
                        break
                    elif answer[i] > lion[i]:
                        break

            # 위에서 더해줬던 부분을 빼는거 같은데 이유를 모르겠음
            if n > 0:
                lion[10] -= n
            return

        # 화살을 쏘는데 남은
        if info[idx] + 1 <= n:  # 남은 화살수가 어피치의 점수 +1 보다 클때
            lion[idx] = info[idx] + 1  # 라이언이 점수를 어디 위해 채워주고
            func(n - info[idx] - 1, lion, idx + 1)  # 뺀만큼 다시 쏜다
            lion[idx] = 0  # 돌고 나면 초기화
        func(n, lion, idx + 1)  # 이건 어피치가 이기는 부분

    lion = [0] * 11
    cha = 1
    answer = []
    func(n, lion, 0)

    return answer if answer else [-1]
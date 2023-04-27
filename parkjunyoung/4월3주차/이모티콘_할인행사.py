# 이모티콘 할인 행사
from itertools import product


def solution(users, emoticons):
    answer = []
    num1 = len(emoticons)
    num2 = len(users)
    sale = [10, 20, 30, 40]
    sales = list(product([10, 20, 30, 40], repeat=num1))
    max_cnt = 0
    max_hap = 0
    # 일단 순열을 다돌면서 가격정하고 구매하기
    for i in range(len(sales)):                                      # 중복순열에서 나온 할인율
        user_hap = [0] * num2                                        # 유저의 이모티콘 가격의 합
        cnt = 0                                                      # 서비스 가입자 수
        for j in range(num1):
            temp = int(emoticons[j] * ((100 - sales[i][j]) * 0.01))  # 해당이모티콘의 가격
            for k in range(num2):
                if users[k][0] <= sales[i][j]:                       # user의 할인율보다 클 경우
                    user_hap[k] += temp                              # 구매
        # print(user_hap)

        # 이모티콘을 살지 말지 정하고 가입자수 정하기
        for j in range(num2):
            if user_hap[j] >= users[j][1]:                           # 가격이상 이면
                cnt += 1                                             # 가입자 늘리고
                user_hap[j] = 0                                      # 구매가격 0
        # print(sum(user_hap), cnt)

        # 가입자의 최대값이 먼저고 그다음이 가격
        if cnt >= max_cnt:
            if cnt == max_cnt:                                       # 가입자수가 최대값이랑 같다면
                max_hap = max(max_hap, sum(user_hap))                # 구매가격 최대값 비교
            else:
                max_hap = sum(user_hap)                              # 아니면 갱신
            max_cnt = cnt                                            # 갱신

    answer = [max_cnt, max_hap]
    return answer
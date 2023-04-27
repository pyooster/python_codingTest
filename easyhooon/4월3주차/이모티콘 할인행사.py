# 1. 이모티콘 플러스 가입자 늘리는것 > 2. 이모티콘 판매액을 최대한 늘리는 것
# n 명에게 이모티콘 m 개를 판매
# emoticons 들의 할인율을 다 정해놓고 다 정한 다음에 결과를 갱신하도록
# discount_rates = [0.1, 0.2, 0.3, 0.4]
discount_rates = [10, 20, 30, 40]
answer = [0, 0]


def check(users, emoticons, n, m, choose_discount_rates):
    discounted_emoticon_prices = []
    emoticon_plus_cnt = 0
    total_sales = 0

    # 이모티콘의 할인율이 적용된 가격을 구함
    for i in range(m):
        # 2. 두번째 디버깅 해맨지점
        # 부동 소수점 계산 고려
        # discounted_emoticon_prices.append(int(emoticons[i] * (1 - choose_discount_rates[i])))
        discounted_emoticon_prices.append(emoticons[i] * (100 - choose_discount_rates[i]) // 100)


    # 이모티콘 플러스 구독자와, 총 판매액을 구함
    for i in range(n):
        # 각 사람당 이모티콘 구매 비용
        sales = 0
        for j in range(m):
            # 1. 첫번째 디버깅 해맨지점
            # print("sales", sales)
            # 이모티콘 구독을 하는 경우
            # 해당 반복문이 계산 이후로 옮겨져야 한다
            # if sales >= users[i][1]:
            #     print("emoticon plus subscribe", sales, users[i][1])
            #     emoticon_plus_cnt += 1
            #     break
            # else:
            if users[i][0] <= choose_discount_rates[j]:
                sales += discounted_emoticon_prices[j]
                # print("after", sales)

        # 이모티콘 구독을 하는 경우
        if sales >= users[i][1]:
            # print("emoticon plus subscribe", sales, users[i][1])
            emoticon_plus_cnt += 1
        # 이모티콘 플러스 구독을 안하는 경우
        else:
            total_sales += sales

    # print(emoticon_plus_cnt, total_sales)
    return emoticon_plus_cnt, total_sales


def dfs(users, emoticons, cnt, n, m, choose_discount_rates):
    if cnt == m:
        emoticon_plus_cnt, total_sales = check(users, emoticons, n, m, choose_discount_rates)
        # 정답 갱신
        # 1) 이모티콘 구독자 수가 더 많으면 2) 판매액이 높으면

        # 이모티콘 구독자 수가 더 많으면 무조건 갱신
        if emoticon_plus_cnt > answer[0]:
            answer[0] = emoticon_plus_cnt
            answer[1] = total_sales

        # 이모티콘 구독자 수가 같을 경우
        elif emoticon_plus_cnt == answer[0]:
            # 총 판매액이 더 크면 갱신
            if total_sales > answer[1]:
                answer[1] = total_sales
        return

    # 4개의 할인율 중에 m개 골라서 넣기, 중복을 허용(중복 순열)
    for i in range(4):
        choose_discount_rates.append(discount_rates[i])
        dfs(users, emoticons, cnt + 1, n, m, choose_discount_rates)
        choose_discount_rates.pop()


def solution(users, emoticons):
    n = len(users)
    m = len(emoticons)

    dfs(users, emoticons, 0, n, m, [])

    print(answer)
    return answer

# 3. 세번째 디버깅 해맨 지점
# 이거 남겨 놓으니까 테케 19, 20 틀렸다.. 테케 테스트 한거는 지우자..
# solution([[40, 10000], [25, 10000]], [7000, 9000])
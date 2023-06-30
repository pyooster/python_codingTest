# 유효기간이 지났다면 반드시 수집된 개인정보는 파기해야 함
# 오늘 날짜로 파기해야 할 개인정보 번호들을 구하려 함
# 모든 달은 28일 까지 있다고 가정
def solution(today, terms, privacies):
    temp = today.split(".")
    today = []
    for t in temp:
        today.append(int(t))
    rule = {}
    # 1 <= term <= 100
    for term in terms:
        term_key = term[0]
        term_value = int(term[1:])
        rule[term_key] = rule.get(term_key, 0) + term_value

    print(rule)

    n = len(privacies)
    answer = []
    for i in range(n):
        temp = privacies[i].split(" ")
        start_day_str = temp[0]
        rule_key = temp[1]
        temp = start_day_str.split(".")
        start_day = []

        for t in temp:
            start_day.append(int(t))

        end_day = []
        plus_year = rule[rule_key] // 12
        plus_month = rule[rule_key] % 12
        # print(plus_year, plus_month)

        end_day.append(start_day[0] + plus_year)
        end_day.append(start_day[1] + plus_month)
        end_day.append(start_day[2] - 1)

        # print(end_day)

        # 날짜가 1일이었을때 - 1 해서 0
        if end_day[2] == 0:
            end_day[1] -= 1
            end_day[2] = 28

        # 문제의 부분
        if end_day[1] > 12:
            # print(end_day[1], end_day[1] // 12, end_day[1] % 12)
            add_plus_year = end_day[1] // 12

            end_day[0] += add_plus_year
            end_day[1] -= (12 * add_plus_year)

        # print(start_day, end_day)

        # 날짜 비교
        if today[0] > end_day[0]:
            answer.append(i + 1)
            continue

        elif today[0] == end_day[0]:
            if today[1] > end_day[1]:
                answer.append(i + 1)
                continue
            elif today[1] == end_day[1]:
                if today[2] > end_day[2]:
                    answer.append(i + 1)
                    continue

    # print(answer)

    return answer
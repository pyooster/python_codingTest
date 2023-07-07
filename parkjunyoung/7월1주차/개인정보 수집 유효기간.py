# 개인정보 수집 유효기간

def solution(today, terms, privacies):
    answer = []
    a, b, c = map(int, today.split("."))

    # 오늘 날짜를 day 로 계산
    today = a * 12 * 28 + b * 28 + c

    # 유효기간 dict
    term = {}
    for i in terms:
        x, y = i.split()
        term[x] = int(y)

    # 유효기간을 더한 날짜를 day로 계산
    for i in range(len(privacies)):
        day, t = privacies[i].split()
        y, m, d = map(int, day.split("."))
        m += term[t]
        check = y * 12 * 28 + m * 28 + d

        # 오늘이 유효기간보다 크거나 같으면 만료 (하루를 빼야하는데 그냥 같으면 만료로 해석)
        if today >= check:
            answer.append(i + 1)

    # 오름차순으로 정렬
    answer.sort()
    return answer
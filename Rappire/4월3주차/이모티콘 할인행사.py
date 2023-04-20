discount = [0.1, 0.2, 0.3, 0.4]


def solution(users, emoticons):
    global length
    global best
    # 가입자, 판매액
    best = [0, 0]
    length = len(emoticons)
    check([], users, emoticons)
    return best


def check(arr, users, emoticons):
    if len(arr) < length:
        for i in range(4):
            arr.append(discount[i])
            check(arr, users, emoticons)
            arr.pop()
    else:
        total_purchase = 0
        emoticon_user = 0
        for percent, total in users:
            purchase = 0
            flag = True
            for dis, price in zip(arr, emoticons):
                if int(dis * 100) >= percent:
                    purchase += price * (1 - dis)
                    if purchase >= total:
                        emoticon_user += 1
                        flag = False
                        break
            if flag:
                total_purchase += purchase
        if best[0] < emoticon_user:
            best[0] = emoticon_user
            best[1] = total_purchase
        elif best[0] == emoticon_user and best[1] < total_purchase:
            best[1] = total_purchase

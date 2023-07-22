# 전화 번호 목록


def solution(phone_book):
    answer = True
    # 정렬
    phone_book.sort()
    # 반복
    for i in range(len(phone_book)-1):
        # 그다음 전화번호의 앞부분[:] 이 현재 전화번호의 길이랑 비교해서 접두어 이면
        if phone_book[i] in phone_book[i+1][:len(phone_book[i])]:
            answer = False
            return answer
    return answer


phone_book = ["12","123","1235","567","88"]

print(solution(phone_book))



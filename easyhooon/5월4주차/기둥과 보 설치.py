
def solution(n, build_frame):
    answer = []

    # a: 구조물의 종류 0 -> 기둥, 1 -> 보
    # b: 구조물을 설치 할지 말지 0 -> 삭제, 1 -> 설치
    for x, y, a, b in build_frame:
        # 기둥 설치
        if b == 1 and a == 0:
            # 바닥에 있는 경우 무조건 설치 가능
            if y == 0:
                answer.append([x, y, a])

            # 바닥에 있지 않은 경우
            else:
                # 해당 지점 밑에 기둥이 있는 경우
                temp = [x, y - 1, 0]
                # 해당 지점 밑 왼쪽에 보가 있는 경우
                temp2 = [x - 1, y, 1]
                # 해당 지점 밑 오른쪽에 보가 있는 경우
                temp3 = [x, y, 1]

                if temp in answer or temp2 in answer or temp3 in answer:
                    answer.append([x, y, a])
        # 보 설치
        elif b == 1 and a == 1:
            # 왼쪽 아래 기둥 설치
            temp = [x, y - 1, 0]
            # 오른쪽 아래 기둥 설치
            temp2 = [x + 1, y - 1, 0]
            # 왼쪽에 보 설치
            temp3 = [x - 1, y, 1]
            # 오른쪽 보 설치
            temp4 = [x + 1, y, 1]

            if (temp in answer) or (temp2 in answer) or (temp3 in answer and temp4 in answer):
                answer.append([x, y, a])

        # 기둥 제거
        elif b == 0 and a == 0:
            # 위에 기둥이 있다면
            if [x, y + 1, 0] in answer:
                # 왼쪽 오른쪽 바쳐 줄 수 없다면
                if [x - 1, y + 1, 1] not in answer and [x, y + 1, 1] not in answer:
                    continue

            # 오른쪽 위 보가 있다면
            if [x, y + 1, 1] in answer:
                # 다른쪽 기둥이 버티고 있지 않거나 양쪽 보가 연결 되어 있지 않다면
                if [x + 1, y, 0] not in answer and ([x + 1, y + 1, 1] not in answer or [x - 1, y + 1, 1] not in answer):
                    continue

            # 왼쪽 위 보가 있다면
            if [x - 1, y + 1, 1] in answer:
                # 다른쪽 기둥이 버티고 있지 않거나 양쪽 보가 연결 되어 있지 않다면
                if [x - 1, y, 0] not in answer and ([x, y + 1, 1] not in answer or [x - 2, y + 1, 1] not in answer):
                    continue

            # 다른 곳으로 인해 버티기 가능
            answer.pop(answer.index([x, y, a]))

        # 보 제거
        elif b == 0 and a == 1:
            # 왼쪽 위 기둥이 있다면
            if [x, y, 0] in answer:
                # 아래쪽 기둥도 없고 왼쪽에 바쳐줄 보도 없다면
                if [x, y - 1, 0] not in answer and [x - 1, y, 1] not in answer:
                    continue

            # 오른쪽 위 기둥이 있다면
            if [x + 1, y, 0] in answer:
                # 아래쪽 기둥도 없고 오른쪽에 바쳐줄 보도 없다면
                if [x + 1, y - 1, 0] not in answer and [x + 1, y, 1] not in answer:
                    continue

            # 왼쪽에 보가 있다면
            if [x - 1, y, 1] in answer:
                # 아래 둘다 기둥이 없다면
                if [x - 1, y - 1, 0] not in answer and [x, y - 1, 0] not in answer:
                    continue

            # 오른쪽에 보가 있다면
            if [x + 1, y, 1] in answer:
                # 아래 둘다 기둥이 없다면
                if [x + 1, y - 1, 0] not in answer and [x + 2, y - 1, 0] not in answer:
                    continue

            # 다른 곳으로 인해 버티기 가능
            answer.pop(answer.index([x, y, a]))

    answer.sort(key=lambda x: (x[0], x[1], x[2]))

    return answer
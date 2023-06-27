# 거리두기 확인하기

def check(place):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    for i in range(5):
        for j in range(5):
            # 만약 사람이면
            if place[i][j] == "P":
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if 0 <= nx < 5 and 0 <= ny < 5:
                        if place[nx][ny] == "P":
                            return 0
            # 만약 빈테이블이면 근처에 2명이 있으면 실패
            elif place[i][j] == "O":
                cnt = 0
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if 0 <= nx < 5 and 0 <= ny < 5:
                        if place[nx][ny] == "P":
                            cnt += 1
                            if cnt >= 2:
                                return 0

    return 1


def solution(places):
    answer = []
    for place in places:
        answer.append(check(place))

    return answer


places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places))

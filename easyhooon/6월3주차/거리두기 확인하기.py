# 각 대기실 별로 거리두기 지키면 1, 한명 이라도 안지키면 0을 담아 return
# 3차원 배열임

answer = []


def check(candidates, place):
    for sx, sy, ex, ey in candidates:
        for x in range(sx, ex + 1):
            for y in range(sy, ey + 1):
                if place[x][y] == 'O':
                    return False

        for x in range(ex, sx + 1):
            for y in range(sy, ey + 1):
                if place[x][y] == 'O':
                    return False

        for x in range(sx, ex + 1):
            for y in range(ey, sy + 1):
                if place[x][y] == 'O':
                    return False

        for x in range(ex, sx + 1):
            for y in range(ey, sy + 1):
                if place[x][y] == 'O':
                    return False

    return True


def is_possible(people, place):
    # 맨하탄 거리가 2 이하인 사람들의 조합을 구함
    candidates = []
    for i in range(len(people) - 1):
        for j in range(i + 1, len(people)):
            dist = abs(people[i][0] - people[j][0]) + abs(people[i][1] - people[j][1])
            if dist <= 2:
                # 맨해튼 거리가 1 이하인 위치 관계가 존재 -> 무조건 불가능
                if dist <= 1:
                    answer.append(0)
                    return
                # 맨해튼 거리가 2, 거리 두기 조건을 위반할 수 있는 후보
                else:
                    sx = people[i][0]
                    sy = people[i][1]
                    ex = people[j][0]
                    ey = people[j][1]

                    candidates.append((sx, sy, ex, ey))

    if check(candidates, place):
        answer.append(1)
    else:
        answer.append(0)


def solution(places):
    for place in places:
        people = []
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    people.append((i, j))

        is_possible(people, place)

    return answer


# print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
print(solution([["OOPOO", "OPOOO", "OOOOO", "OOOOO", "OOOOO"]]))
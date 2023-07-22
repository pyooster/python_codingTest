# 자물쇠와 열쇠

# 시계 방향으로 회전하기
def turn(key):
    temp = list(map(list, zip(*key[::-1])))
    # for i in temp:
    #     print(i)
    return temp


def solution(key, lock):
    answer = True
    num1 = len(lock)
    num2 = len(key)
    # 키가 들어갈 자리를 담는 배열
    lock_point = []
    for i in range(num1):
        for j in range(num1):
            if lock[i][j] == 0:
                lock_point.append((i+num2-1, j+num2-1))
    cnt = len(lock_point)

    # key의 총개수 확인
    key_cnt = 0
    for i in range(num2):
        for j in range(num2):
            if key[i][j] == 1:
                key_cnt += 1

    # 배열을 자물쇠를 기준으로 양 옆을 키의 길이 -1 만큼씩 추가
    num3 = num1 + 2*num2 - 2
    pan = [[0 for _ in range(num3)] for _ in range(num3)]

    # 자물쇠를 가운데 배치
    for i in range(num1):
        for j in range(num1):
            if lock[i][j] == 1:
                pan[i+num2-1][j+num2-1] = 1
    # for i in pan:
    #     print(i)


    def check(i, j):
        temp_lock = 0
        temp_key = 0
        # key의 범위 만큼 탐색
        for r in range(num2):
            for c in range(num2):
                # 각 점에서 만약 키값이 1 이고
                if key[r][c] == 1:
                # 그점이 lock point이면
                    if (i+r, j+c) in lock_point:
                        temp_lock += 1
                # 그점이 0이라면
                    if pan[i+r][j+c] == 0:
                        temp_key += 1
        # 키에 다 맞아들어가고
        if cnt == temp_lock:
            # 키가 범위를 벋어나도 배치가 된다면
            if key_cnt == temp_key:
                return True
        return False


    for _ in range(4):
        #끝까지 탐색할 필요는 없음
        for i in range(num3-num2+1):
            for j in range(num3-num2+1):
                # check
                answer = check(i, j)
                if answer:
                    return answer
        # 회전
        key = turn(key)
    return answer


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
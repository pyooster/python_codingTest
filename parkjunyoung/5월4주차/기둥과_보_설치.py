def check(x, y, a, ans):
    # 기둥인가
    if a == 0:
        # 바닥위에 있거나
        if y == 0:
            return 1
        # 보의 한쪽 끝 부분 위에 있거나
        if ((x - 1, y, 1) in ans) or ((x, y, 1) in ans):
            return 1
        # 다른 기둥위에 있거나
        if (x, y - 1, 0) in ans:
            return 1
        return 0

    # 보인가
    if a == 1:
        # 한쪽 끝 부분이 기둥위에 있거나
        if ((x, y - 1, 0) in ans) or ((x + 1, y - 1, 0) in ans):
            return 1
        # 양쪽 끝부분이 다른보와 동시에 연될되어있거나
        if ((x - 1, y, 1) in ans) and ((x + 1, y, 1) in ans):
            return 1
        return 0


def solution(n, build_frame):
    ans = set()
    for i in build_frame:
        # x,y 좌표, a 기둥 or 보, b 설치 or 삭제
        x, y, a, b = i[0], i[1], i[2], i[3]
        # 설치
        if b == 1:
            if check(x, y, a, ans) == 1:
                ans.add((x, y, a))
        # 삭제
        if b == 0:
            # 삭제
            ans.remove((x, y, a))
            # 조건이 충족하는지 확인
            for x1, y1, a1 in ans:
                if check(x1, y1, a1, ans) == 1:
                    continue
                else:
                    # 아니면 다시 추가
                    ans.add((x, y, a))
                    break
    ans = list(ans)
    ans.sort()
    return ans
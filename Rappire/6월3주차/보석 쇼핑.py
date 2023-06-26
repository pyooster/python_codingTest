from collections import defaultdict


def solution(gems):
    answer = []
    minNum = 10e10
    gemNum = len(set(gems))
    length = len(gems)
    gemdict = defaultdict(int)
    pos = 0
    count = 0
    for start in range(length):
        while count < gemNum and pos < length:
            if gemdict[gems[pos]] == 0:
                count += 1
            gemdict[gems[pos]] += 1
            pos += 1

        if count == gemNum:
            if minNum > pos - start:
                minNum = pos - start
                answer = [start + 1, pos]

        if gemdict[gems[start]] == 1:
            count -= 1
        gemdict[gems[start]] -= 1

    return answer

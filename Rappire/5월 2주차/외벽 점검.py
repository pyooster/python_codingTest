from itertools import permutations


def solution(n, weaks, dist):
    answer = int(10e10)
    weakPos = weaks[:]
    for i in weaks:
        weakPos.append(i + n)
    for i, weak in enumerate(weaks):
        for friends in permutations(dist):
            pos = weak
            count = 0
            for friend in friends:
                pos += friend
                count += 1
                if pos >= weakPos[i + len(weaks) - 1]:
                    answer = min(answer, count)
                    break
                else:
                    for next in weakPos:
                        if next > pos:
                            pos = next
                            break
    if answer == int(10e10):
        return -1
    return answer

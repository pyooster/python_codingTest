from collections import defaultdict
from bisect import bisect_left


def solution(infos, queries):
    infomap = defaultdict(list)
    for info in infos:
        for i in range(16):
            temp = info.split()
            if i & 8 == 8:
                temp[0] = "-"
            if i & 4 == 4:
                temp[1] = "-"
            if i & 2 == 2:
                temp[2] = "-"
            if i & 1 == 1:
                temp[3] = "-"
            infomap["".join(temp[:-1])].append(int(temp[4]))
            print("".join(temp[:-1]))

    for key in infomap.keys():
        infomap[key].sort()

    answer = []

    for query in queries:
        temp = query.split(" and ")
        finalTemp = temp[-1].split()
        queryString = "".join(temp[:-1]) + finalTemp[0]
        answer.append(
            len(infomap[queryString])
            - bisect_left(infomap[queryString], int(finalTemp[1]))
        )

    return answer

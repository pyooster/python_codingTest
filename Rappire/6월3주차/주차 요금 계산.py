from math import ceil
from collections import defaultdict


def solution(fees, records):
    recordDict = {}
    totalDict = defaultdict(int)
    answer = []

    for record in records:
        time, carNum, history = record.split()
        time = time2num(time)
        carNum = int(carNum)
        if recordDict.get(carNum, -1) != -1:
            inTime = recordDict.pop(carNum)
            totalDict[carNum] += time - inTime
        else:
            recordDict[carNum] = time

    inTime = 23 * 60 + 59

    for key in recordDict.keys():
        totalDict[key] += inTime - recordDict[key]

    keys = list(totalDict.keys())
    keys.sort()
    for key in keys:
        answer.append(calFee(totalDict[key], fees))
    return answer


def time2num(time):
    hour, minute = map(int, time.split(":"))
    return hour * 60 + minute


def calFee(total, fees):
    if total > fees[0]:
        return fees[1] + ceil((total - fees[0]) / fees[2]) * fees[3]
    return fees[1]

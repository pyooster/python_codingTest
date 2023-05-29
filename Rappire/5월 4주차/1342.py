import sys
from math import factorial
from collections import Counter


def search(str, strLength):
    global count
    if strLength == length:
        count += 1
        return
    flag = True
    num = 0
    if len(str) == 0 or countString[str] == 0:
        for i in countString.values:
            if i == 1:
                num += 1
            elif i != 0:
                flag = False
                break
        if flag:
            count += factorial(num)
            return
    for i in countString:
        if str != i and countString[i] > 0:
            countString[i] -= 1
            search(i, strLength + 1)
            countString[i] += 1


input = sys.stdin.readline

string = input().rstrip()
countString = Counter(string)
length = len(string)
count = 0

search("", 0)
print(count)

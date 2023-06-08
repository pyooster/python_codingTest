import sys
from itertools import permutations

input = sys.stdin.readline


def check(x, y, z, count):
    global answer
    if x < 0:
        x = 0
    if y < 0:
        y = 0
    if z < 0:
        z = 0
    if x == 0 and y == 0 and z == 0:
        answer = min(count, answer)
        return
    if dp[x][y][z] > count:
        dp[x][y][z] = count
        for dx, dy, dz in list(permutations([9, 3, 1])):
            check(x - dx, y - dy, z - dz, count + 1)


N = int(input())
maxInt = sys.maxsize
dp = [[[maxInt for i in range(61)] for i in range(61)] for i in range(61)]

scv = list(map(int, input().split()))

while len(scv) < 3:
    scv.append(0)

x, y, z = scv
answer = maxInt
check(x, y, z, 0)

print(answer)

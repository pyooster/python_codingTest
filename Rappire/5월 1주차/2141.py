import sys

input = sys.stdin.readline
N = int(input())
villages = []
humanSum = 0

for i in range(N):
    X, A = map(int, input().split())
    villages.append([X, A])

    humanSum += A

villages.sort()
humanSum /= 2

check = 0
for village in villages:
    check += village[1]
    if check >= humanSum:
        print(village[0])
        break

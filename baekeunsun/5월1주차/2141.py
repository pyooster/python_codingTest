# 우체국
import sys
input = sys.stdin.readline

N = int(input())
village =[]
human = 0

for _ in range(N):
    distance, people = map(int,input().split())
    village.append([distance,people])
    human += people

village.sort()
tmp = 0
answer = 0

for i in range(N):
    tmp += village[i][1]
    if tmp >= (human/2) :
        answer = village[i][0]
        break

print(answer)

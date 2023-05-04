# 거짓말
from collections import deque

N, M = map(int,input().split())
know = list(map(int,input().split()))
meet = list({0} for _ in range(N+1))
party = []

know.pop(0)

for i in range(M):
    tmp = list(map(int,input().split()))
    for i in range(1,tmp[0]+1):
        for j in range(1,tmp[0]+1):
            meet[tmp[i]].add(tmp[j])
    party.append(tmp[1:])

queue = deque(know)
while queue:
    tmp = queue.popleft()
    for i in (meet[tmp]):
        if i in know :
            continue
        else :
            know.append(i)
            queue.append(i)
        

answer = 0
for i in range(M):
    intersection = list(set(know) & set(party[i]))
    if intersection :
        continue
    else :
        answer += 1

print(answer)

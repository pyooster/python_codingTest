import sys
input = sys.stdin.readline
from collections import defaultdict

N, d, k, c = map(int,input().split())
sushi = []
for _ in range(N):
    sushi.append(int(input()))
sushi.extend(sushi)

left = 0
right = 0
max_cnt = 0
eat = defaultdict(int)

eat[c] += 1

for right in range(len(sushi)):
    eat[sushi[right]] += 1

    if right >= k-1:
        max_cnt = max(max_cnt,len(eat))
        print(max_cnt)
        eat[sushi[left]] -= 1
        if eat[sushi[left]] == 0:
            del eat[sushi[left]]
        left += 1
        
print(max_cnt)
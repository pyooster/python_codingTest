# 개똥벌레
import sys
input = sys.stdin.readline

N, H = map(int,input().split())
up = [0]*(H+1)
down = [0]*(H+1)

for i in range(N):
    tmp = int(input())
    if i%2 == 0 :
        down[tmp] += 1
    else:
        up[tmp] += 1

for i in range(H-1,0,-1):
    up[i] += up[i+1]
    down[i] += down[i+1]
min_count = 0
min_num = sys.maxsize

for i in range(1,H+1):
    tmp = up[i] + down[H-i+1]
    if min_num == tmp :
        min_count += 1
        continue
    if min_num > tmp :
        min_num = tmp
        min_count = 1

print(min_num, min_count)

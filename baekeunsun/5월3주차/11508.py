# 2+1 세일
import sys
input = sys.stdin.readline

N = int(input())
buy = list(int(input()) for _ in range(N))
buy.sort(reverse=True)
answer = []

for i in range(N//3):
    answer += buy[i*3:i*3+2]
    
for j in range(N%3):
    answer.append(buy[-1-j])

print(sum(answer))

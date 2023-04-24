import sys

input = sys.stdin.readline
day = int(input())
Week = [0 for i in range(day + 1)]


now = 0
for i in range(day):
    T, P = map(int, input().split())
    finish = T + i
    now = max(Week[i], now)
    if finish > day:
        continue
    Week[finish] = max(now + P, Week[finish])

print(max(Week[-1], now))

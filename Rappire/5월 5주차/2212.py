import sys

input = sys.stdin.readline

n = int(input())
k = int(input())
sensor = list(map(int, input().split()))
sensor.sort()

if k >= n:
    print(0)
    sys.exit()

calc = []

for i in range(n - 1):
    calc.append(sensor[i + 1] - sensor[i])

calc.sort(reverse=True)
k -= 1
print(sum(calc[k:]))

# 사이클 게임
import sys
input = sys.stdin.readline


def find(n):
    if cycle[n] == n:
        return n
    else:
        cycle[n] = find(cycle[n])
        return cycle[n]


def union(a, b):
    x = find(a)
    y = find(b)
    if x < y:
        cycle[y] = x
    elif x > y:
        cycle[x] = y


n, m = map(int, input().split())
cycle = [i for i in range(n)]

ans = 0
for i in range(1, m+1):
    a, b = map(int, input().split())
    # 두 부모가 같다면
    if find(a) == find(b):
        # 몇번째 차례인지 
        ans = i
        # 멈춰
        break
    # 아니면 유니온
    union(a, b)


print(ans)
# print(cycle)
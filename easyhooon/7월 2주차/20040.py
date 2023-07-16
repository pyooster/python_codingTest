# 사이클이 완성 되었다면 몇번째 차례에 처음으로 사이클이 완성된 것인지를 출력
# Union-Find
import sys

sys.setrecursionlimit(10 ** 6)

si = sys.stdin.readline

# 3 <= n <= 500,000
# 3 <= m <= 1,000,000
n, m = map(int, si().split())

uf = [0] * n

for i in range(n):
    uf[i] = i


def find(x):
    if uf[x] == x:
        return x

    root_node = find(uf[x])
    uf[x] = root_node

    return root_node


def union(x, y):
    x = find(x)
    y = find(y)
    uf[x] = y


answer = 0
for i in range(1, m + 1):
    x, y = map(int, si().split())
    # 사이클이 생성 되었는지 검사
    if find(x) == find(y):
        answer = i
        break
    # 사이클이 아니면 union 연산 진행
    else:
        union(x, y)

print(answer)

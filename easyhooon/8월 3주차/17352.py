# 여러분의 다리가 되어 드리겠습니다!

# 유니온 파인드를 통해 연결하는 것이 아닌, 유니온 파인드의 결과로 연결되지 않은 두 섬을 찾는 문제
import sys
sys.setrecursionlimit(10**6)

si = sys.stdin.readline


def union(x, y):
    x = find(x)
    y = find(y)
    uf[x] = y


def find(x):
    if uf[x] == x:
        return x

    root_node = find(uf[x])
    uf[x] = root_node
    return root_node


n = int(si())
uf = [0] * (n + 1)

for i in range(1, n + 1):
    uf[i] = i

for _ in range(n - 2):
    x, y = map(int, si().split())
    union(x, y)

roots = set()
for i in range(1, n + 1):
    roots.add(uf[i])
    # roots.add(uf[i]) -> 틀림
    # roots.add(find(i))

# print(roots[0], roots[1])
roots = list(roots)
# print(roots)
print(roots[0], roots[1])

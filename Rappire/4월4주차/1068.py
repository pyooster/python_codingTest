import sys

input = sys.stdin.readline

N = int(input())
parent = list(map(int, input().split()))
K = int(input())

parent[K] = -2
stack = [K]
while len(stack) > 0:
    now = stack.pop()
    parent[now] = -2
    for pos, i in enumerate(parent):
        if i == now:
            stack.append(pos)

parent_set = set(parent)
count = 0
for pos, i in enumerate(parent):
    if i != -2 and pos not in parent_set:
        count += 1

print(count)

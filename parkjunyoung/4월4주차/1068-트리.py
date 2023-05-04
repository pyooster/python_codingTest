# 트리

N = int(input())
node = list(map(int, input().split()))
remove_node = int(input())


def dfs(num):
    node[num] = 51
    for i in range(N):
        if node[i] == num:
            dfs(i)


dfs(remove_node)
# print(node)

cnt = 0
for i in range(N):
    if node[i] != 51:
        if i not in node:
            cnt += 1

print(cnt)
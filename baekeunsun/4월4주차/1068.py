# 트리
def dfs(node):
    tree[node] = -2
    for i in range(N):
        if node == tree[i]: # 자식의 자식
            dfs(i)
            
N = int(input())
tree = list(map(int, input().split()))
E = int(input())

dfs(E)
answer = 0

for i in range(N):
    if tree[i] != -2 and i not in tree:
        answer += 1

print(answer)

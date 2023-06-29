# 음악프로그램

N, M = map(int, input().split())
check = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
cnt = [0 for _ in range(N+1)]

for _ in range(M):
    temp = list(map(int, input().split()))
    a = temp.pop(0)
    for i in range(a-1):
        check[temp[i]].append(temp[i+1])
        cnt[temp[i+1]] += 1

# print(check)
# print(cnt)
ans = []
while len(ans) < N:
    flag = 0
    for i in range(1, N+1):
        if not cnt[i] and visited[i] == 0:
            flag = 1
            ans.append(i)
            visited[i] = 1
            for j in check[i]:
                cnt[j] -= 1
    if flag != 1:
        ans = [0]
        break

for i in ans:
    print(i)
# 거짓말
from collections import deque

N, M = map(int, input().split())
true = list(map(int, input().split()))
true = true[1:]
know_member = [0] * (N+1)                       # 진실을 아는 사람 체크
for i in true:
    know_member[i] = 1
# print(know_member)

party_member = []                               # 파티별 사람 체크


tree = [[] for _ in range(N+1)]                 # 관계 트리?
for i in range(M):                              # 모든 파티를 돌면서 관계를 체크한다음 bfs 돌려야댐
    person = list(map(int, input().split()))
    num = person[0]
    person = person[1:]
    party_member.append(person)                 # 파티 맴버에 넣어주고
    for j in range(num):
        for k in range(j+1, num):
            tree[person[j]].append(person[k])   # 관계 연결
            tree[person[k]].append(person[j])   # 쌍방향


# print(tree)


def bfs(a):
    q = deque()
    q.append(a)
    while q:
        now = q.popleft()
        for i in tree[now]:             # 연결된 사람들 중
            if not know_member[i]:      # 아는 사람에 체크가 안되어있으면
                know_member[i] = 1      # 체크하고
                q.append(i)             # 다시 추가


for i in range(len(know_member)):
    if know_member[i]:                  # 내가 알고있다면
        bfs(i)                          # 나랑 만난사람들 체크

# print(know_member)
# print(party_member)
ans = M
for i in party_member:                  # 해당 파티에서
    for j in i:                         # 참가한 사람중에
        if know_member[j] == 1:         # 거짓말을 안다면
            ans -= 1                    # -1
            break
print(ans)
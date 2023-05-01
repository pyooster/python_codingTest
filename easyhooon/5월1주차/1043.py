# 거짓말

# 이야기의 진실을 아는 사람들에겐 진실을 이야기 할 수 밖에 없다
# 어떤 사람이 어떤 파티에서는 진실을 듣고, 또 다른 파티에서는 과장된 이야기를 들었을 때도, 지민이는 거짓말쟁이로 알려지게 된다.
# 지민이는 모든 파티에 참가
# 거짓말쟁이로 알려지지 않으면서, 과장된 이야기를 할 수 있는 파티 개수의 최댓값

import sys

si = sys.stdin.readline

# 사람의 수, 파티의 수
n, m = map(int, si().split())
uf = [0] * (n + 1)

for i in range(1, n + 1):
    uf[i] = i


def union(x, y):
    x = find(x)
    y = find(y)
    # 이렇게 판단 과정을 내리면 안될거 같은게 이후의 파티가 이전 파티에 영향을 미치지 못하고 있음
    # -> 마지막에 검사할대 find 를 한번 더 돌려주면 됨
    if x in true_arr and y not in true_arr:
        uf[y] = x

    elif y in true_arr and x not in true_arr:
        uf[x] = y

    elif x in true_arr and y in true_arr:
        return
    else:
        min_num = min(x, y)
        max_num = max(x, y)
        uf[max_num] = min_num


def find(x):
    if uf[x] == x:
        return x

    root_node = find(uf[x])
    uf[x] = root_node

    return root_node

# 이야기의 진실을 아는 사람의 수, 목록
# 진실을 아는 사람이 존재하면 해당 파티에는 과장을 못함
# 진실을 아는 사람이 없는 파티만을 체크하면 됨
true_arr = list(map(int, si().split()))

# 진실을 아는 사람이 없으면 모든 파티에 과장된 이야기 가능
if true_arr[0] == 0:
    print(m)
    exit(0)

true_arr = true_arr[1:]

parties = []

# 각 파티마다 오는 사람의 수와 번호
# 쭉 나열되어 있어서 짝짓는게 까다롭네
# i, i + 1 로 하자 ㅇㅇ
for _ in range(m):
    party = list(map(int, si().split()))
    if party[0] != 1:
        for i in range(1, party[0]):
            # print(party[i], party[i + 1])
            union(party[i], party[i + 1])

    parties.append(party[1:])

# 과장된 이야기를 할 수 있는 '파티 수', '사람 수' (x)
answer = 0

# print(true_arr)

for party in parties:
    # print(party)
    flag = True
    for elem in party:
        # if uf[elem] in true_arr:
        if find(elem) in true_arr:
            flag = False
            break

    if flag:
        answer += 1


# print(uf)
print(answer)


import sys
input = sys.stdin.readline

n, m = map(int, input().split())
truePerson = set(map(int, input().split()[1:]))

parties = []
for _ in range(m):
    parties.append(set(map(int, sys.stdin.readline().split()[1:])))

# 진실을 말해야하는 파티: True, 아닌 파티: False
cnt = [False] * m

for _ in range(m):# 진실만 말하는 파티 찾기 위해
    for i, partyPeople in enumerate(parties):
        if truePerson & partyPeople: # 진실을 아는 사람이 파티에 있다면(교집합이면)
            cnt[i] = True 
            truePerson = truePerson | partyPeople # 파티의 모든 사람이 진실을 알아야함

print(cnt.count(False)) # 과장된 이야기를 할 수 있는 파티의 수
# 개똥벌레

N, H = map(int, input().split())
sizes = []
for i in range(N):
    size = int(input())
    sizes.append(size-1)

up = [0] * H
down = [0] * H

for i in range(N):
    if i % 2 == 0:
        down[sizes[i]] += 1              # 몇층짜리가 몇개가 있는지 확인
    if i % 2 != 0:
        up[sizes[i]] += 1

print(up)
print(down)

hap_up = [N//2]                          # 위쪽 높이에 있는 장애물 수
hap_down = [N//2]                        # 아래쪽

for i in range(1, H):
    temp_up = up[i-1]
    hap_up.append(hap_up[i-1]-temp_up)   # 이전 높이 만큼 빼고 남은 높이 더하기

    temp_down = down[i-1]
    hap_down.append(hap_down[i-1]-temp_down)

hap_down.reverse()                       # 역순

print(hap_up)
print(hap_down)

hap = []
for i in range(H):
    hap.append(hap_up[i] + hap_down[i])  # 각 높이에 있는 장애물 수
ans = min(hap)
cnt = hap.count(ans)
print(ans, cnt)




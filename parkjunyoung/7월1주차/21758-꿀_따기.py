# 꿀 따기

N = int(input())
honey = list(map(int, input().split()))
hap = [0 for _ in range(N)]
hap[0] = honey[0]
for i in range(1, N):
    hap[i] = hap[i-1] + honey[i]


# print(honey)
# print(hap)
ans = 0
# 벌 벌 꿀
for i in range(1, N-1):
    # 첫번째 벌의 꿀 누적합 + 두번째 벌의 꿀 누적합 - 두번째 벌의 위치의 꿀
    ans = max(ans, (hap[N-1] - honey[0]) + (hap[N-1] - hap[i]) - honey[i])
# 꿀 벌 벌
for i in range(1, N-1):
    # 첫번째 벌의 꿀 누적합 + 두번째 벌의 꿀 누적합 - 두번째 벌의 위치의 꿀
    ans = max(ans, hap[N-2] + hap[i-1] - honey[i])
# 벌 꿀 벌
for i in range(1, N-1):
    # 양끝에 벌이 자리를 잡으면 최대일것이고 중간에 꿀통이 위치
    ans = max(ans, hap[N-2] - honey[0] + honey[i])


print(ans)
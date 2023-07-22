# 정육점

N, M = map(int, input().split())
arr = []
for i in range(N):
    w, p = map(int, input().split())
    arr.append((p, w))

# 가격 오름차순, 무게 내림차순
arr = sorted(arr, key=lambda x: (x[0], -x[1]))

# 누적합으로 가격을 누적
sort_p = [(0, 0)] * (N+1)
for i in range(1, N+1):
    sort_p[i] = (arr[i-1][0], arr[i-1][1] + sort_p[i-1][1])

# 누적합으로 무게을 누적
hap_w = [(0, 0)] * (N+1)
for i in range(1, N+1):
    if sort_p[i-1][0] == sort_p[i][0]:
        hap_w[i] = (hap_w[i-1][0] + sort_p[i][0], sort_p[i][1])
    else:
        hap_w[i] = sort_p[i]

ans = 2147483648

# 최소 가격 찾기
for i in range(1, N+1):
    if hap_w[i][1] >= M:
        ans = min(ans, hap_w[i][0])

if ans == 2147483648:
    print(-1)
else:
    print(ans)


print(arr)
hap_w.pop(0)
print(hap_w)

# # 반례 답 15 오답 18
# 11 55
# 2 1
# 2 1
# 2 1
# 3 1
# 6 2
# 7 3
# 7 3
# 8 3
# 10 3
# 8 3
# 8 3
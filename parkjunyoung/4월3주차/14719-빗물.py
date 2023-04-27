# 빗물

H, W = map(int, input().split())
arr = list(map(int, input().split()))

top = max(arr)
idx = arr.index(top)
# print(top, idx)

ans = 0
height = 0
# 왼쪽
for i in range(idx+1):          # 최고 높이까지
    if height < arr[i]:         # 왼쪽 벽을 갱신
        height = arr[i]
    else:                       # 왼쪽 벽보다 낮으면 물이 채워짐
        ans += height-arr[i]    # 왼쪽 높이 - 현재높이
        # print(ans)

height = 0

# 오른쪽
for i in range(W-1, idx, -1):
    if height < arr[i]:
        height = arr[i]
    else:
        ans += height - arr[i]
        # print(ans)

print(ans)
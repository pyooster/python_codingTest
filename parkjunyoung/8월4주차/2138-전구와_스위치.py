# 전구와 스위치

N = int(input())
arr_1 = list(input())
for x in range(len(arr_1)):
    if arr_1[x] == '0':
        arr_1[x] = False
    else:
        arr_1[x] = True
arr_2 = arr_1.copy()
ans = list(input())
for x in range(len(ans)):
    if ans[x] == '0':
        ans[x] = False
    else:
        ans[x] = True


cnt_1 = 0
cnt_2 = 1


# 처음스위치를 패스
for i in range(1, N):
    # i-1 이랑 같지 않으면
    if arr_1[i - 1] != ans[i - 1]:
        cnt_1 += 1
        # 앞 현재 뒤 변경
        arr_1[i] = not arr_1[i]
        arr_1[i - 1] = not arr_1[i - 1]
        # 마지막일때는 index 에러 방지
        if i != N - 1:
            arr_1[i + 1] = not arr_1[i + 1]




if arr_1 != ans:
    cnt_1 = 9999999


# 처음 스위치 누를때
arr_2[0] = not arr_2[0]
arr_2[1] = not arr_2[1]

for i in range(1, N):
    if arr_2[i - 1] != ans[i - 1]:
        cnt_2 += 1
        # 앞 현재 뒤 변경
        arr_2[i] = not arr_2[i]
        arr_2[i - 1] = not arr_2[i - 1]
        # 마지막일때는 index 에러 방지
        if i != N - 1:
            arr_2[i + 1] = not arr_2[i + 1]

if arr_2 != ans:
    cnt_2 = 9999999

if cnt_1 == 9999999 and cnt_2 == 9999999:
    print(-1)
else:
    print(min(cnt_1, cnt_2))
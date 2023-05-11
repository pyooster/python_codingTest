# 카드 섞이

N = int(input())
P = list(map(int, input().split()))
S = list(map(int, input().split()))
change = [i for i in range(N)]
cnt = 0
arr = []
for i in range(N):
    arr.append(P[i])

while 1:
    flag = 1
    for i in range(N):
        if change[i] % 3 != arr[i]:
            flag = 0
    if flag == 1:
        print(cnt)
        exit()

    cnt += 1
    temp = []
    flag = 1
    for j in range(N):
        if S[change[j]] != j:
            flag = 0
        temp.append(S[change[j]])
    change = temp

    if flag == 1:
        cnt = -1
        print(cnt)
        exit()

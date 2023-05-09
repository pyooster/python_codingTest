import sys

input = sys.stdin.readline

N = int(input())
arrP = list(map(int, input().split()))
arrS = list(map(int, input().split()))
arr = arrP[:]
count = 0
while 1:
    flag = True
    for i in range(len(arr)):
        if arr[i] != i % 3:
            flag = False
            break
    if flag:
        print(count)
        exit()

    temparr = [0 for i in range(N)]
    for i, next in enumerate(arrS):
        temparr[next] = arr[i]
    arr = temparr
    flag = True
    count += 1

    for x, y in zip(arrP, arr):
        if x != y:
            flag = False
            break
    if flag:
        print(-1)
        exit()

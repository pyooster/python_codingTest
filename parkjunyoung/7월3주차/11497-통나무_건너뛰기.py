# 통나무 건너뛰기

from collections import deque
T = int(input())

for tc in range(T):
    N = int(input())
    temp = list(map(int, input().split()))
    # 정렬
    temp.sort()
    temp = deque(temp)
    # 2분탐색? 느낌
    arr = [0] * N
    l = 0
    r = N-1
    # 왼쪽 오른쪽에 작은거를 계속 넣어준다
    for i in range(N//2):
        arr[l] = temp.popleft()
        arr[r] = temp.popleft()
        l += 1
        r -= 1
    # 다돌고도 1개가 남을 수있으니까 가운데 넣어준다
    if temp:
        arr[N//2] = temp.popleft()

    ans = 0
    # print(arr)
    for i in range(N):
        ans = max(ans, abs(arr[i] - arr[i-1]))
    print(ans)



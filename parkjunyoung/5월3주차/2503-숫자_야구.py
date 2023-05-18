# 숫자 야구
from itertools import permutations
N = int(input())
arr = list(permutations(['1', '2', '3', '4', '5', '6', '7', '8', '9'], 3))
ans = [1] * len(arr)

for i in range(N):
    num, s, b = map(int, input().split())
    num = list(str(num))
    for j in arr:
        strike = 0
        ball = 0
        # print(j, num)
        for k in range(3):
            for l in range(3):
                if j[k] == num[l]:
                    if k != l:
                        ball += 1
                    if k == l:
                        strike += 1
        temp = arr.index(j)
        if ans[temp] != 0 and s == strike and b == ball:
            ans[temp] = 1
        else:
            ans[temp] = 0
# print(ans)
print(sum(ans))

# 두 배열의 합
from collections import Counter

T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

list_A = A                            # 부분집합 넣을거
list_B = B                            # 부분집합 넣을거

for i in range(n):                    # 완탐하면서 각원소를 더하면서 추가
    hap = A[i]
    for j in range(i+1, n):
      hap += A[j]
      list_A.append(hap)

for i in range(m):
    hap = B[i]
    for j in range(i+1, m):
      hap += B[j]
      list_B.append(hap)

# 완탐으로 탐색하면 시간 초과 난다
# check = 0
# for i in list_A:
#     for j in list_B:
#         if i+j == T:
#             check += 1
# print(check)
# 범위가 너무 커서 완탐은 시간초과

ans = 0
# A의 부 배열을 Counter 를 통해 어떤 숫자가 몇개있는지 탐색
num = Counter(list_A)

# B의 부 배열의 합을 돌면서 T - B부배열의 합 = A부배열의 합 을 이용해서 ans 값을 추가
for i in range(len(list_B)):
    ans += num[T-list_B[i]]
print(ans)
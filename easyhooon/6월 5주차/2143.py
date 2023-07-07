# 두 배열의 합
# 각각의 배열의 합의 순서쌍을 count map 에 저장해서 각각의 count map 을 비교, 갯수가 몇개인지
import sys

si = sys.stdin.readline

t = int(si())
n = int(si())
a = list(map(int, si().split()))
m = int(si())
b = list(map(int, si().split()))
a_sum = {}
b_sum = {}
answer = 0
# 1 3 1 2
# 1개 4C1 = 4
# 1 3 1 2
# 2개 4C2 = 6
# 4 2 3 4 5 3
# 3개 4C3 = 4
# 5 6 4 6
# 4개 4C4 = 1
# 7
# 1: 2
# 2: 2
# 3: 3
# 4: 3
# 5: 2
# 6: 2
# 7: 1

# 1 3 2 3C1 + 3C2 + 3C3 = 3 + 3 + 1 = 7
# 1: 1
# 2: 1
# 3: 2
# 4: 1
# 5: 1
# 6: 1

# 5
# 1 4
# 2 3
# 3 2
# 4 1

# 부 배열의 합: 해당 값이 몇번 나올수 있는지-> 맵에 저장해둠
# A[1] + A[4] + B[3] 이건 없음
# A[3] + A[4] + B[3] 이건 있고
# 부 배열의 합이라는게 연속되 인덱스여야 하는듯
# for i in range(1, n + 1):
#     combination_i = list(combinations(a, i))
#     for elem in combination_i:
#         a_sum[sum(elem)] = a_sum.get(sum(elem), 0) + 1
#
# for j in range(1, m + 1):
#     combination_j = list(combinations(b, j))
#     for elem in combination_j:
#         b_sum[sum(elem)] = b_sum.get(sum(elem), 0) + 1

for i in range(n):
    for j in range(i, n):
        sub_a = a[i: j + 1]
        a_sum[sum(sub_a)] = a_sum.get(sum(sub_a), 0) + 1

for i in range(m):
    for j in range(i, m):
        sub_b = b[i: j + 1]
        b_sum[sum(sub_b)] = b_sum.get(sum(sub_b), 0) + 1

# print(a_sum)
# print(b_sum)

# 한쪽이 전부 차지하면 안되니까 각각의 합의 범위는 1, ~ (t -1)
# 아 T 에 음의 정수도 들어올 수 있음 (-1,000,000,000 <= T <= 1,000,000,000)
# 이런 음의 인덱스 때문에 HashMap 을 사용한 것
# for i in range(1, t):
#     # answer += a_sum[i] * b_sum[t - i] -> KeyError
#     # print(a_sum.get(i, 0), b_sum.get(t - i, 0))
#     answer += a_sum.get(i, 0) * b_sum.get(t - i, 0)

for key in a_sum.keys():
    # answer += a_sum[key] * b_sum[t - key] -> KeyError
    answer += a_sum.get(key, 0) * b_sum.get(t - key, 0)

print(answer)
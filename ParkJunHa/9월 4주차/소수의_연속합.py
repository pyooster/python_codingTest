# 에라토스테네스의 채
# import math
# n = 0
# is_prime = [1 for _ in range(n+1)]
# is_prime[0], is_prime[1] = 0, 0

# for i in range(2, int(math.sqrt(n) + 1)):
#     if is_prime[i]:
#         for j in range(2, n // i+1):
#             is_prime[i*j] = 0

import sys
import math

sys.setrecursionlimit(10 ** 8)
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
if n == 1:
    print(0)
    exit()

# 2 3 5 7 11 13 17 19 23 29 31 37 ...
# 4,000,000 == 2000^2
MAX = 4000000
is_prime = [1 for _ in range(n + 1)]
is_prime[0], is_prime[1] = 0, 0

for i in range(2, int(math.sqrt(n)) + 1):
    if is_prime[i]:
        for j in range(2, n // i + 1):
            is_prime[i * j] = 0  # 소수의 배수들은 다 소수가 아니므로 0으로 만듦

p = []
for i in range(2, n + 1):
    if is_prime[i]:
        p.append(i)

cnt = 0
i, j = len(p) - 1, len(p) - 1
cur = p[-1]
while 0 <= i <= j and 0 <= j < len(p):
    if cur > n:
        cur -= p[j]
        j -= 1

    else:
        if cur == n:
            cnt += 1
        i -= 1
        if i < 0:
            break
        cur += p[i]
print(cnt)
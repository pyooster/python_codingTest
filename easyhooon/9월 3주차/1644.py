import sys
import math

si = sys.stdin.readline

n = int(si())

is_prime = [True] * (n + 1)
sqrt_of_n = int(math.sqrt(n))

for i in range(2, sqrt_of_n + 1):
    if not is_prime:
        continue

    else:
        j = 2
        while i * j <= n:
            if is_prime[i * j]:
                is_prime[i * j] = False
            j += 1

prime = []
for i in range(2, n + 1):
    if is_prime[i]:
        prime.append(i)

# print(prime)

if n == 1:
    print(0)
    exit(0)

left = 0
right = 0
cnt = prime[0]
answer = 0

while left <= right < len(prime):
    if cnt <= n:
        if cnt == n:
            # print(prime[left], prime[right])
            answer += 1

        # right index out of range
        right += 1
        if right == len(prime):
            break
        cnt += prime[right]

    else:
        cnt -= prime[left]
        left += 1

print(answer)

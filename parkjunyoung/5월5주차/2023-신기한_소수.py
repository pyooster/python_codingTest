# 신기한 소수

import math

def is_prime_num(n):
    for i in range(2, int(math.sqrt(n))+1): # n의 제곱근을 정수화 시켜준 후 + 1
        if n % i == 0:
            return False
    return True


N = int(input())


def dfs(num):
    if len(list(str(num))) == N:
        print(num)
    else:
        for i in range(1, 10):
            if i % 2 == 0:
                continue
            if is_prime_num(num*10 + i):
                dfs(num*10 + i)


dfs(2)
dfs(3)
dfs(5)
dfs(7)
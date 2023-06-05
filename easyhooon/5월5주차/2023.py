# 신기한 소수

import sys

si = sys.stdin.readline

n = int(si())

candidate_number = [1, 2, 3, 5, 7, 9]


def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


def dfs(curr_num, num):
    if curr_num == n:
        print(num)
        return

    for elem in candidate_number:
        num = num * 10 + elem
        # 소수 판정
        if is_prime(num):
            dfs(curr_num + 1, num)
        num -= elem
        num //= 10


dfs(0, 0)
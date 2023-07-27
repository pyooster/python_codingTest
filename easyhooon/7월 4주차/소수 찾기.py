from itertools import permutations
import math


# len(numbers) <= 7
# 11과 011은 같은 숫자로 취급

def solution(numbers):
    answer = 0
    # print(list(numbers))
    lst = []
    for i in range(1, len(numbers) + 1):
        for elem in list(permutations(list(numbers), i)):
            lst.append(elem)

    num_list = []
    for elem in lst:
        num_list.append(int("".join(elem)))
    # print(num_list)
    num_list.sort()
    n = num_list[-1]

    ###  에라토스테네스의 체
    is_prime = [True for _ in range(n + 1)]
    sqrt_of_num = int(math.sqrt(n))

    for i in range(2, sqrt_of_num + 1):
        if not is_prime[i]:
            continue
        else:
            j = 2
            while i * j <= n:
                if is_prime[i * j]:
                    is_prime[i * j] = False
                j += 1
    ###

    visited = [False for _ in range(n + 1)]

    for elem in num_list:
        if elem < 2:
            continue

        if is_prime[elem] and not visited[elem]:
            visited[elem] = True
            answer += 1

    return answer
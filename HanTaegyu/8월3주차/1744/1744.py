"""
    Solution code for "BaekJoon 수 묶기".

    - Problem link: https://www.acmicpc.net/problem/1744

    입력
        - N : (1 <= N <= 49)
        - N개의 수 : (-1_000 ~ +1_000)

    출력
        총합을 출력

"""
from sys import stdin as input
from typing import List

# input = open('./test1.txt')

plus = []
other = []


def tie(data: List[int], answer: int) -> int:
    while 1 < len(data):
        num1, num2 = data.pop(), data.pop()
        answer += max(num1 + num2, num1 * num2)
    return answer


def remain_number() -> None:
    if other:
        if plus:
            return plus.pop() + other.pop()
        else:
            return other.pop()
    else:
        if plus:
            return plus.pop()
        else:
            return 0


def main() -> None:
    N = int(input.readline())
    for _ in range(N):
        num = int(input.readline())

        if 0 < num:
            plus.append(num)
        else:
            other.append(num)

    answer = 0

    plus.sort()
    answer = tie(plus, answer)

    other.sort(reverse=True)
    answer = tie(other, answer)

    answer += remain_number()
    print(answer, end="")


if __name__ == '__main__':
    main()
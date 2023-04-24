# 문자열 폭발
# 폭발은 문자열에 폭발 문자열이 없을 때 까지 계속된다.
# 문자열의 길이 최대 1,000,000
import sys
from collections import deque

si = sys.stdin.readline

origin = si().strip()
bomb_origin = si().strip()
bomb_size = len(bomb_origin)
arr = list(origin)
bomb_arr = list(bomb_origin)

stack = deque()


def get_string():
    tmp = []
    for _ in range(bomb_size):
        tmp.append(stack.pop())

    return "".join(reversed(tmp))


for i in range(len(arr)):
    stack.append(arr[i])
    # 스택의 원소의 개수가 폭발 문자열보다 많거나, 마지막에 들어온 원소가 폭발 문자열의 마지막 원소인 경우
    # deque 으록 stack 을 구현에서 먼저 들어온 원소가 어떤 인덱스에 들어있는지 헷갈린다.
    if len(stack) >= len(bomb_arr) and stack[-1] == bomb_arr[-1]:
        # 스택의 끝에서부터 폭발 문자열의 길이 만큼 슬라이싱 해서 판별하고 뽑음 -> stack을 문자열로 통변환해서 시초
        # 원소를 폭발 문자열의 길이만큼 꺼낸 다음에 문자열로 변환해야함
        tmp = get_string()
        if tmp != bomb_origin:
            for i in range(bomb_size):
                stack.append(tmp[i])

        # print(stack)

if len(stack) == 0:
    print("FRULA")
else:
    print("".join(stack))

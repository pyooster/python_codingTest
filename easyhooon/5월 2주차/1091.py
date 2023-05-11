import sys

si = sys.stdin.readline

num = int(si())
idx = list(map(int, si().split()))
init_state = idx[:]
shuffle = list(map(int, si().split()))


def is_sorted(idx, num):
    for i in range(num):
        if idx[i] != (i % 3):
            return False
    return True


count = 0

while not is_sorted(idx, num):
    count += 1
    # 카드 섞기
    copy = idx[:]
    for i in range(num):
        idx[shuffle[i]] = copy[i]
    # 카드가 섞기 전 맨 처음 상태인지 확인
    for i in range(num):
        if init_state[i] != idx[i]:
            break
        if i == num - 1:
            # 싸이클이 발생, 아무리 섞어도 종료 조건을 충족하지 못함
            print(-1)
            exit(0)

print(count)

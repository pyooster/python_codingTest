import sys
from collections import Counter

si = sys.stdin.readline


def dfs(curr_num, pre):
    global answer

    # 행운의 문자열 생성
    if curr_num == len(s):
        answer += 1

    for k in cnt.keys():
        # 현재 단어가 이전 단어일 경우와 현재 단어의 개수가 0일 경우 다음 단어를 확인
        if k == pre or cnt[k] == 0:
            continue

        cnt[k] -= 1
        dfs(curr_num + 1, k)
        cnt[k] += 1


s = list(map(str, si().strip()))

# 문자의 개수를 딕셔너리로 변환
cnt = Counter(s)
answer = 0

dfs(0, '')

print(answer)
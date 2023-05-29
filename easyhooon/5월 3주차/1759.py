# 암호 만들기
import sys

# 증가하는 순 -> 순서가 정해져 있다 (순열)
# 더 나은 풀이 확인

si = sys.stdin.readline

l, c = map(int, si().split())

selected = [0]
alphabets = [" "] + list(map(str, si().split()))
visited = [False] * (c + 1)
alphabets.sort()


def is_vowel(x):
    return x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u'


def dfs(k):
    if k == l + 1:
        vowel = 0
        consonant = 0

        for i in range(1, l + 1):
            if is_vowel(alphabets[selected[i]]):
                vowel += 1
            else:
                consonant += 1

        if vowel >= 1 and consonant >= 2:
            answer = ""
            for i in range(1, l + 1):
                answer += alphabets[selected[i]]
            print(answer)

    for i in range(1, c + 1):
        # 이전에 뽑은 값과도 비교가 필요
        if not visited[i] and i > selected[k - 1]:
            selected.append(i)
            visited[i] = True
            dfs(k + 1)
            visited[i] = False
            selected.pop()


dfs(1)
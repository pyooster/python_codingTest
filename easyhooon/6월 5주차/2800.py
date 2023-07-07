# 괄호 제거
# 스택을 통해 괄호의 쌍(문자열에서의 인덱스)을 pair 로 리스트에 저장하여
# 이들을 재귀를 통해 순서를 정하여 출력
# 출력된 순서쌍중 겹치는 것이 존재하면 하나만 출력(set 자료구조 이용)
# 스택은 list 로 대체
# 쌍을 제거해서 나올 수 있는 서로 다른 식을 사전 순으로 출력
import sys
from itertools import combinations

si = sys.stdin.readline

stack = []

exp = si().strip()
pair_list = []
n = len(exp)

for i in range(n):
    if exp[i] == '(':
        stack.append(i)
    elif exp[i] == ')':
        j = stack.pop()
        pair_list.append((j, i))

# print(pair_list)
# pair_list.sort() # 필요 없음
# print(pair_list)
m = len(pair_list)

# 출력이 까다롭다

# 괄호를 한개도 안 고른거는 출력 x
# 중복되는거 한번씩만 출력
answer = []

for i in range(1, m + 1):
    combinations_i = list(combinations(pair_list, i))
    for elem in combinations_i:
        exp_visited = [False] * len(exp)
        for j in range(len(elem)):
            exp_visited[elem[j][0]] = True
            exp_visited[elem[j][1]] = True

        exp_str = ""
        for k in range(len(exp)):
            if not exp_visited[k]:
                exp_str += exp[k]

        answer.append(exp_str)
        for j in range(len(elem)):
            exp_visited[elem[j][0]] = False
            exp_visited[elem[j][1]] = False

answer = list(set(answer))
answer.sort()
for elem in answer:
    print(elem)







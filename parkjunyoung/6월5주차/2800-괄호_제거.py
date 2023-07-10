# 괄호 제거
from itertools import combinations

arr = input()
temp = list(arr)

# 괄호의 쌍을 넣을 stack
stack = []
# 모든 괄호 쌍의 idx
all_lr = []
for i in range(len(temp)):
    if temp[i] == '(':
        stack.append(i)
    elif temp[i] == ')':
        l_idx = stack.pop()
        all_lr.append((l_idx, i))
# 부분집합으로 모든 괄호의 경우의 수를 담는다
case = []
for i in range(len(all_lr)+1):
  case = case + list(combinations(all_lr, i))
ans = []
# 첫번째는 공집합이라 패스
for i in range(1, len(case)):
    now = temp.copy()
    # 그냥 pop을 해버리면 index 에러가 발생해서 idx를 따로 뽑는다
    sort_case = []
    for (a, b) in case[i]:
        sort_case.append(a)
        sort_case.append(b)
    # 큰 idx 부터 pop 해야하므로 정렬한번 해주고
    sort_case.sort(reverse=True)
    for j in sort_case:
        now.pop(j)
    # 수식을 완성하고 추가
    now = ''.join(now)
    # 여기서 중복이 발생할 수 있음
    if now not in ans:
        ans.append(now)

# 정렬해서 출력
ans.sort()
for i in ans:
    print(i)
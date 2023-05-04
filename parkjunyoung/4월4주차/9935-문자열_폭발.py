# 문자열 폭발

word = list(input())
boom = list(input())
num = len(boom)
stack = []
for i in word:                        # 전체 리스트를 돌면서
    stack.append(i)                   # 하나씩 체크
    if num <= len(stack):             # 현재 길이가 폭발 길이보다 길고
        if boom == stack[-num:]:      # 스택의 뒤에서 체크했을때 폭발 문자열과 같으면
            for j in range(num):      # 길이만큼 pop
                stack.pop()

    # print(stack)

if stack:
    print("".join(stack))
else:
    print("FRULA")
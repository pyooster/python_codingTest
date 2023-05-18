from itertools import combinations

l, c = map(int, input().split())
alpha = sorted(list(input().split())) # 입력을 받자마자 정렬해주어야함

aeiou = ['a','e','i','o','u']
total_case = list(combinations(alpha,l))
remove_pw = []

for case in total_case:
    m_cnt = 0

    for c in case:
        if c in aeiou:
            m_cnt += 1

    if m_cnt < 1: # 모음이 1개 미만이면
        remove_pw.append(case)

    elif l - m_cnt < 2: # 자음이 2개 미만이라면
        remove_pw.append(case)

answer = set(total_case) - set(remove_pw)
answer = list(answer)
answer = sorted(answer)

for ans in answer:
    answ = sorted(list(ans))
    for i in answ:
        print(i, end='')
    print("")

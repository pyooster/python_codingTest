# 괄호 추가하기
import sys

si = sys.stdin.readline

INT_MIN = -sys.maxsize

max_result = INT_MIN

def calc(num, op):
    while op:
        oper = op.pop(0)
        n1, n2 = num.pop(0), num.pop(0)
        if oper == '+':
            num.insert(0, n1 + n2)
        elif oper == '-':
            num.insert(0, n1 - n2)
        elif oper == '*':
            num.insert(0, n1 * n2)

    return num[0]


# 백트래킹
# cnt: 현재까지 고려한 연산자 수
# num 숫자 모음
# op 연산자 모음
def choose(cnt, num, op):
    global max_result

    # 종료 조건
    if cnt == n // 2 or len(num) == 1:
        max_result = max(max_result, calc(num, op))
        return

    # 연산자를 사용하지 않는 경우
    choose(cnt + 1, num[:], op[:])

    # 연산자를 사용하는 경우
    # -> num 리스트에서 2개의 원소가 있어야 하므로 조건을 추가
    if cnt + 1 < len(num):
        n1, n2 = num[cnt], num[cnt + 1]
        oper = op[cnt]
        if oper == '+':
            num[cnt] = n1 + n2
        elif oper == '-':
            num[cnt] = n1 - n2
        elif oper == '*':
            num[cnt] = n1 * n2

        # 인덱스로 배열의 원소를 제거
        # del num[cnt + 1]
        # del op[cnt]
        num.pop(cnt + 1)
        op.pop(cnt)

        choose(cnt + 1, num[:], op[:])

n = int(si())
exp = si().strip()

# 숫자와 연산자를 분리하여 담기
num = []
op = []

for i in range(n):
    if i % 2 == 0:
        num.append(int(exp[i]))
    else:
        op.append(exp[i])

choose(0, num, op)

print(max_result)

# 잠수함 식별
import re
import sys

si = sys.stdin.readline

str = si().strip()

# 정상적인 잠수함의 엔진소리는 (100~1~|01)~ 패턴을 따름
# 이를 정규식으로 표현하면 다음과 같음
# '+' 는 앞선 문자가 1번 이상 반복됨을 나타냄
# '|' 는 OR 연산을 의미
# 즉, '100' 다음에 1이 하나 이상 나오고, 그 다음에 '1'이 하나 이상 나오거나, '0' 다음에 '1'이 오는 패턴이 반복되는 것을 찾음
pattern = re.compile('(100+1+|01)+')
# fullmatch() 함수는 문자열 전체가 정규식 패턴과 일치하는지 확인
match = pattern.fullmatch(str)

if match:
    print('SUBMARINE')
else:
    print('NOISE')

# 잠수함식별

import re
# 정규식으로 풀면 아주 간단한 문제였음
sign = input()
# 규칙 컴파일, 패턴 생성
# + 는 100~1 | 는 or 느낌
pattern = re.compile('(100+1+|01)+')
# fullmatch로 패턴 일치 확인
ans = pattern.fullmatch(sign)

if ans:
    print("SUBMARINE")
else:
    print("NOISE")
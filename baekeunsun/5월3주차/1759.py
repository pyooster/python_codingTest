# 암호 만들기
# 전체 combinations 한 코드
from itertools import combinations
import sys 
input=sys.stdin.readline

L, C = map(int,input().split())
string = sorted(input().split())
words = combinations(string, L)

for word in words :
    count = 0
    for w in word :
        if w in 'aeiou' :
            count += 1
    if count >= 1 and (L-count) >= 2 :
        print(''.join(word))
        
# 암호 만들기
# 자음 모음 나누어서 combinations 한 코드
import itertools
import sys 
input=sys.stdin.readline

L, C = map(int,input().split())
string = list(map(str,input().split()))

ja = []
mo = []

for i in string :
    if i in ['a','e','i','o','u'] :
        ja.append(i)
    else :
        mo.append(i)

answer = []
tmp = []
for n in range(1,min(len(ja)+1, L-1)):
    for case1 in (itertools.combinations(ja, n)) :
        for case2 in (itertools.combinations(mo, L - n)):
            tmp = list(case1 + case2)
            tmp.sort()
            answer.append(tmp)
answer.sort()

for i in answer :
    print(*i, sep='')
    
    

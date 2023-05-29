# 숫자 야구
N = int(input())
number = [True] * 1000    # 이 중 세자리수만 사용

for i in range(123, 1000):
    tmp = str(i)
    if tmp[0] == tmp[1] or tmp[1] == tmp[2] or tmp[0] == tmp[2]:
        number[i] = False
    if '0' in tmp:
        number[i] = False
        
for i in range(0, N):
    target, strike, ball = map(int,input().split())
    
    for num in range(123, 1000):
        strike_cnt = 0
        ball_cnt = 0
        
        for t in range(0, 3):
            for n in range(0, 3):
                if str(target)[t] == str(num)[n]:
                    if t == n :
                        strike_cnt += 1
                    else :
                        ball_cnt += 1

        if strike != strike_cnt or ball != ball_cnt:
            number[num] = False

print(number[123:1000].count(True))

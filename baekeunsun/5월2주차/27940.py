# 가지 산사태
# for문 두번 넣은거 혹시 설명 부족했을까 싶어서 밑에 추가 해놨습니다~!

# 최종 풀이
import sys
input = sys.stdin.readline

N, M, K = map(int,input().split())   # 농장층수, 비 횟수, 버틸수있는 빗물 양

total = 0
for i in range(1,M+1):
    t, r = map(int,input().split())  # 1층~t층, r만큼 비
    total += r
    if total > K :
        print(i,1)
        sys.exit()
    
print(-1)

# 중간 풀이
import sys
input = sys.stdin.readline

N, M, K = map(int,input().split())   # 농장층수, 비 횟수, 버틸수있는 빗물 양
farm = [0]*(N+1)

total = 0
for i in range(1,M+1):
    t, r = map(int,input().split())  # 1층~t층, r만큼 비
    farm[t] += r
    total += r
    if total > K :
        tmp = 0
        for j in range(N,0,-1):
            tmp += farm[j]
            if tmp > K :
                print(i, j)
                sys.exit()
    
print(-1)


# 2+1 세일

N = int(input())
C = []
for i in range(N):
    temp = int(input())
    C.append(temp)
ans = 0
cnt = 0
C.sort(reverse=True)
# print(C)
for i in range(N):
    cnt += 1
    if cnt == 3:
        C[i] = 0
        cnt = 0

print(sum(C))
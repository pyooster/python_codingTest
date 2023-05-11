# 물병
N, K = map(int,input().split()) # 물병 수, 한버에 옮길 수 있는 물병 수
count = 0

while bin(N).count('1') > K:
    N += 1
    count += 1

print(count)

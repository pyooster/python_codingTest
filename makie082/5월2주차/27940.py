import sys
input = sys.stdin.readline # 이거 안해줘도 시간초과 뜸 ㅜ ㅜ

n, m, k = map(int, input().split())

floor = 0
for i in range(m): # 비
    t, r = map(int, input().split()) # 영향이 가는 층, 파괴량

    # 어차피 1층은 항상 영향을 받으니까
    # 1층만 고려해주면 됨!
    floor += r
    if floor > k:
        print(i+1, 1)
        exit()

print(-1)
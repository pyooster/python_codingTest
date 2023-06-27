# 치킨 배달

from itertools import combinations

N, M = map(int, input().split())                                 # 도시, 치킨집집의 최대 개수
city = [list(map(int, input().split())) for _ in range(N)]       # 도시 입력
house = []                                                       # 집
chicken = []                                                     # 치킨집
for i in range(N):                                               # 전체탐색
    for j in range(N):
        if city[i][j] == 1:                                      # 집에 추가
            house.append((i, j))
        elif city[i][j] == 2:                                    # 치킨집에 추가
            chicken.append((i, j))

arr = list(combinations(chicken, M))                             # 조합 다 만들기
dis = [0] * len(arr)                                             # 거리의 합
for i in house:                                                  # 집들중에서
    for j in range(len(arr)):                                    # 조합들의
        cnt = 999999                                             # 치킨집과 집사이의 거리
        for k in arr[j]:                                         # 각각의 값의
            cnt = min(cnt, abs(i[0]-k[0])+abs(i[1]-k[1]))        # 거리의 차를 구해서 최소값을 구해서
        dis[j] += cnt                                            # 거리의 합에 추가한다
print(min(dis))                                                  # 최소 거리값
# 벽 부수고 이동하기 4
from collections import deque

N, M = map(int,input().split())
Map = [list(map(int, input())) for _ in range(N)]
group_cnt = 2
group = [0,0]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
visit = list([True]*M for _ in range(N))

def bfs(sx, sy):    
    queue = deque([[sx,sy]])    
    count = 0
    
    while queue :
        x, y = queue.popleft()
        count += 1
        Map[x][y] = group_cnt
        for i in range(4):
            ix = x + dx[i]
            iy = y + dy[i]
            if N > ix >= 0 and M > iy >= 0 and Map[ix][iy] == 0 and visit[ix][iy] == True:
                queue.append([ix,iy])
                visit[ix][iy] = False
    return count

for i in range(N):
    for j in range(M):
        if Map[i][j] == 0 : # 그룹 생성
            visit[i][j] = True
            group.append(bfs(i,j))
            group_cnt += 1
            
for x in range(N) :
    for y in range(M):
        near_list = set()
        tmp = 1
        if Map[x][y] > 1 :
            print(0,end='')
        else :
            for i in range(4):
                ix = x + dx[i]
                iy = y + dy[i]
                if N > ix >= 0 and M > iy >= 0 and Map[ix][iy] not in near_list:
                    near_list.add(Map[ix][iy])
                    tmp += group[Map[ix][iy]]
            print((tmp)%10, end='')
    print()
            

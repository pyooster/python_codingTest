# 미세먼지 안녕!

R, C, T = map(int, input().split())
room = [[int(i) for i in input().split()] for _ in range(R)]

# for i in range(R):
#     print(room[i])

cleaner = []
flag = False
for i in range(R):
    for j in range(C):
        if room[i][j] == -1:
            flag = True
            cleaner = [[i, j], [i+1, j]]
            break
    if flag == True:
        break
# print(cleaner)


def dust():
    copyroom = [[0]*C for _ in range(R)]   # 새로운 배열
    dx = [1, 0, -1, 0]  # 우 상 좌 하
    dy = [0, -1, 0, 1]
    for i in range(R):
        for j in range(C):
            if room[i][j] != 0 and room[i][j] != -1:  # 미세먼지가 잇으면
                temp = room[i][j]
                for k in range(4):      # 4방향을 확인하고
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < R and 0 <= ny < C: # 범위안에 있고
                        if room[nx][ny] != -1:     # 청소기가 아니면
                            copyroom[nx][ny] += (room[i][j]//5)  # 새로운 배열에 확산값을 더해주고
                            temp -= (room[i][j]//5)        # 기존 값은 확산된값을 빼주고
                copyroom[i][j] += temp                     # 4방향 다 확산하면 기존값을 갱신
    for i, j in cleaner:
        copyroom[i][j] = -1

    return copyroom


def wind(room):
    # 위쪽 바람
    for i in range(cleaner[0][0]-1, 0, -1):  # 위에서 아래로
        room[i][0] = room[i-1][0]
    room[0][0] = 0

    for i in range(0, C-1):             # 왼쪽으로
        room[0][i] = room[0][i+1]
    room[0][C - 1] = 0

    for i in range(0, cleaner[0][0]):     # 위로
        room[i][C-1] = room[i+1][C-1]
    room[cleaner[0][0]][C-1] = 0

    for i in range(C-1, 1, -1):         # 오른쪽으로 부는 바람
        room[cleaner[0][0]][i] = room[cleaner[0][0]][i-1]
    room[cleaner[0][0]][1] = 0

    # 아래바람
    for i in range(cleaner[1][0]+2, R): # 위로 부는 바람
       room[i-1][0] = room[i][0]
    room[R-1][0] = 0

    for i in range(0, C-1):     # 왼쪽으로 부는 바람
        room[R-1][i] = room[R-1][i + 1]
    room[R-1][C-1] = 0

    for i in range(R-1, cleaner[1][0], -1):    # 아래로 부는 바람
        room[i][C-1] = room[i-1][C-1]
    room[cleaner[1][0]][C-1] = 0

    for i in range(C-1, 1, -1): # 오른쪽으로 부는 바람
        room[cleaner[1][0]][i] = room[cleaner[1][0]][i-1]
    room[cleaner[1][0]][1] = 0


for i in range(T):
    room = dust()
    wind(room)
    # for j in range(R):
    #     print(room[j])


ans = 0
for i in range(R):
    for j in range(C):
        ans += room[i][j]

ans += 2

print(ans)
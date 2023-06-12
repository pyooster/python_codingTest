import sys
from collections import deque


def moveCheck(x, y):
    for dx, dy in move:
        dx += x
        dy += y
        if 0 <= dx < H and 0 <= dy < W:
            if mapArr[dx][dy] == "#":
                return True
    return False


input = sys.stdin.readline
move = [[1, 0], [-1, 0], [0, 1], [0, -1]]

H, W = list(map(int, input().split()))
mapArr = []
checklist = [[20 for _ in range(W)] for _ in range(H)]

for _ in range(H):
    mapArr.append(list(input().rstrip()))

for i in range(H):
    for j in range(W):
        if mapArr[i][j] == "S":
            start = [i, j]
            break


queue = deque([[start[0], start[1], 0]])
checklist[start[0]][start[1]] = 1

while queue:
    x, y, count = queue.pop()
    nowCheck = moveCheck(x, y)
    if mapArr[x][y] == "E":
        print(count)

    for dx, dy in move:
        dx += x
        dy += y
        if 0 <= dx < H and 0 <= dy < W:
            if checklist[dx][dy] > count and mapArr[dx][dy] != "#":
                checklist[dx][dy] = count
                if nowCheck and moveCheck(dx, dy):
                    queue.appendleft([dx, dy, count])
                else:
                    queue.appendleft([dx, dy, count + 1])

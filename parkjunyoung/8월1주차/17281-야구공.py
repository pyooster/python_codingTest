# 야구공
from itertools import permutations

N = int(input())
arr = [i for i in range(1, 9)]
per = list(permutations(arr, 8))
board = []
for i in range(N):
    temp = list(map(int, input().split()))
    board.append(temp)
ans = 0

for i in per:
    taja = list(i[:3]) + [0] + list(i[3:])
    score = 0
    now = 0
    for j in range(N):
        out = 0
        b1, b2, b3 = 0, 0, 0
        while out < 3:
            if board[j][taja[now]] == 0:
                out += 1
            elif board[j][taja[now]] == 1:
                score += b3
                b1, b2, b3 = 1, b1, b2
            elif board[j][taja[now]] == 2:
                score += (b2 + b3)
                b1, b2, b3 = 0, 1, b1
            elif board[j][taja[now]] == 3:
                score += (b1 + b2 + b3)
                b1, b2, b3 = 0, 0, 1
            elif board[j][taja[now]] == 4:
                score += (b1 + b2 + b3 + 1)
                b1, b2, b3 = 0, 0, 0
            now = (now+1) % 9
    ans = max(ans, score)

print(ans)
def solution(game_board, table):
    puzzlelist = findPuzzle(table)
    emptylist = findEmpty(game_board)
    answer = 0
    for i in emptylist:
        for pos, j in enumerate(puzzlelist):
            if checkSpin(i, j):
                answer += sumpuzzle(j)
                puzzlelist.pop(pos)
                break
    return answer


def sumpuzzle(puzzle):
    count = 0
    for i in puzzle:
        for j in i:
            if j == 1:
                count += 1
    return count


def movecheck(x, y, length):
    move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    arr = []
    for i in move:
        if i[0] + x >= 0 and i[0] + x < length:
            if i[1] + y >= 0 and i[1] + y < length:
                arr.append([i[0] + x, i[1] + y])
    return arr


def checksame(puzzle, empty, puzzlelen):
    for x in range(puzzlelen[0]):
        for y in range(puzzlelen[1]):
            if puzzle[x][y] != empty[x][y]:
                return False
    return True


def checkSpin(puzzle, empty):
    puzzlelen = [len(puzzle), len(puzzle[0])]
    emptylen = [len(empty), len(empty[0])]
    if emptylen[0] != puzzlelen[0] or emptylen[1] != puzzlelen[1]:
        if emptylen[0] != puzzlelen[1] or emptylen[1] != puzzlelen[0]:
            return False
    for i in range(4):
        puzzlelen[0] = len(puzzle)
        puzzlelen[1] = len(puzzle[0])
        if emptylen[0] != puzzlelen[0] or emptylen[1] != puzzlelen[1]:
            puzzle = spin(puzzle)
            continue
        if checksame(puzzle, empty, puzzlelen):
            return True
        puzzle = spin(puzzle)
    return False

 
def spin(puzzle):
    n = len(puzzle)
    m = len(puzzle[0])
    new = [[0] * n for i in range(m)]
    for i in range(n):
        for j in range(m):
            new[j][n - i - 1] = puzzle[i][j]
    return new


def findEmpty(game_board):
    length = len(game_board)
    check = [[0 for i in range(length)] for i in range(length)]
    puzzlelist = []
    for i in range(length):
        for j in range(length):
            if check[i][j] == 1:
                continue
            if game_board[i][j] == 1:
                check[i][j] = 1
                continue
            puzzle = []
            stack = [[i, j]]
            while len(stack) > 0:
                now = stack.pop()
                if check[now[0]][now[1]]:
                    continue
                check[now[0]][now[1]] = 1
                puzzle.append(now)
                nextmove = movecheck(now[0], now[1], length)
                for move in nextmove:
                    if check[move[0]][move[1]] == 0:
                        if game_board[move[0]][move[1]] == 0:
                            stack.append(move)
            puzzlelist.append(reguler(puzzle))
    return puzzlelist


def reguler(puzzle):
    maxl = [-1, -1]
    minl = [55, 55]
    for i in puzzle:
        maxl[0] = max(i[0], maxl[0])
        maxl[1] = max(i[1], maxl[1])
        minl[0] = min(i[0], minl[0])
        minl[1] = min(i[1], minl[1])
    arr = [
        [0 for i in range(maxl[1] - minl[1] + 1)] for i in range(maxl[0] - minl[0] + 1)
    ]
    for i in puzzle:
        x = i[0] - minl[0]
        y = i[1] - minl[1]
        arr[x][y] = 1
    return arr


def findPuzzle(table):
    length = len(table)
    check = [[0 for i in range(length)] for i in range(length)]
    puzzlelist = []

    for i in range(length):
        for j in range(length):
            if check[i][j] == 1:
                continue
            if table[i][j] == 0:
                check[i][j] = 1
                continue
            puzzle = []
            stack = [[i, j]]
            while len(stack) > 0:
                now = stack.pop()
                if check[now[0]][now[1]]:
                    continue
                check[now[0]][now[1]] = 1
                puzzle.append(now)
                nextmove = movecheck(now[0], now[1], length)
                for move in nextmove:
                    if check[move[0]][move[1]] == 0:
                        if table[move[0]][move[1]] == 1:
                            stack.append(move)
            puzzlelist.append(reguler(puzzle))
    return puzzlelist

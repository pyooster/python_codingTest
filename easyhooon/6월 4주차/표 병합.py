def solution(commands):
    answer = []

    # merge 관계를 나타내기 위한 배열 (같은 순서쌍이 들어가 있으면 그 칸들은 merge 되어있다.)
    # 병합된 셀에 접근하기 위해 만든 배열
    merged = [[(i, j) for j in range(51)] for i in range(51)]
    # 실제 값이 들어 있는 배열
    board = [["EMPTY"] * 51 for _ in range(51)]
    print(merged)

    for command in commands:
        if command.startswith("UPDATE"):
            # 병합된 칸이 있다면 해당 칸도 업데이트
            # r, c (value)
            tmp = command.split(" ")
            if len(tmp) == 4:
                r, c, value = int(tmp[1]), int(tmp[2]), tmp[3]
                # print(r, c, merged[r][c])
                # r, c 가 어떤 칸에 merge가 되어있는지 확인 -> r, c 가 아닌 다른 순서쌍(x, y)이 들어있는 경우 -> 다른 순서쌍(x, y) 칸에 merge 되어 있다.
                x, y = merged[r][c]
                # x, y 칸에 value 업데이트
                board[x][y] = value

            # value1 -> value2
            elif len(tmp) == 3:
                value1, value2 = tmp[1], tmp[2]
                for i in range(1, 51):
                    for j in range(1, 51):
                        # value 1 이 들어있는 칸을 전부 value 2로 변경
                        if board[i][j] == value1:
                            board[i][j] = value2

        elif command.startswith("MERGE"):
            tmp = command.split(" ")
            r1, c1, r2, c2 = int(tmp[1]), int(tmp[2]), int(tmp[3]), int(tmp[4])
            # 현재 칸이 어느 칸에 merge 되어 있는지 확인 (r, c) == (x, y) 이면 merge 되지 않은 것
            x1, y1 = merged[r1][c1]
            x2, y2 = merged[r2][c2]

            # 병합하려는 셀에 값이 존재하지 않으면
            if board[x1][y1] == "EMPTY":
                # 병합 하는 칸에 값을 가짐
                board[x1][y1] = board[x2][y2]

            for i in range(51):
                for j in range(51):
                    # (i, j 가 x2, y2 로 merge 되어 있었다면)
                    if merged[i][j] == (x2, y2):
                        # (i, j) 를 (x1, y1) 칸에 merge
                        merged[i][j] = (x1, y1)


        elif command.startswith("UNMERGE"):
            tmp = command.split(" ")
            r, c = int(tmp[1]), int(tmp[2])
            # r, c 가 어떤 칸에 merge 되어 있는지
            x, y = merged[r][c]
            # 머지된 칸의 값을 저장
            tmp_value = board[x][y]
            for i in range(51):
                for j in range(51):
                    # (x, y) 라는 칸에 merge 되어 있는 상태라면
                    if merged[i][j] == (x, y):
                        # unmerge
                        merged[i][j] = (i, j)
                        board[i][j] = "EMPTY"
            # 머지 되었었던 칸의 값으로 update
            board[r][c] = tmp_value

        # r,c
        elif command.startswith("PRINT"):
            tmp = command.split(' ')
            r, c = int(tmp[1]), int(tmp[2])
            # 해당 칸이 병합된 칸이 있는지 (없으면 x, y = r, c)
            x, y = merged[r][c]
            answer.append(board[x][y])

    return answer

# print(solution(["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]))
# print(solution(["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]))
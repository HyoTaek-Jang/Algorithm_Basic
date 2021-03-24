def solution(board, moves):
    answer = 0
    row = len(board)
    col = len(board[0])
    temp = [-1 for i in range(col)]

    get = []
    for move in moves:
        if temp[move - 1] == -1:
            for i in range(row):
                if board[i][move - 1] != 0:
                    get.append(board[i][move - 1])
                    board[i][move - 1] = 0
                    temp[move - 1] = i
                    break
            if temp[move - 1] == -1:
                temp[move - 1] = row - 1
        elif temp[move - 1] != row - 1:
            get.append(board[temp[move - 1] + 1][move - 1])
            board[temp[move - 1] + 1][move - 1] = 0
            temp[move - 1] += 1

        if len(get) >= 2 and get[-1] == get[-2]:
            get.pop()
            get.pop()
            answer += 2

    return answer
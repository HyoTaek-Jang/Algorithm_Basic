def solution(board, moves):
    answer = 0
    row = len(board)

    get = []
    for move in moves:
        for i in range(row):
            if board[i][move - 1] != 0:
                get.append(board[i][move - 1])
                board[i][move - 1] = 0
                break

        if len(get) >= 2 and get[-1] == get[-2]:
            get.pop()
            get.pop()
            answer += 2

    return answer
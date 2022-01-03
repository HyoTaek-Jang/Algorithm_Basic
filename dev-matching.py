from collections import deque


def solution(macaron):
    board = [[0] * 6 for _ in range(6)]

    for cur_macaron in macaron:
        #         마카롱 투하
        for row in range(5, -1, -1):
            if board[cur_macaron[0]][row] == 0:
                board[cur_macaron[0]][row] = cur_macaron[1]
                break

        #         연속된거 있는지 확인
        for row in range(5, -1, -1):
            for col in range(6):
                result = connectCehck(board)

                if result != -1:
                    print(result)

    answer = []
    return answer


def connectCehck(board):
    for row in range(5, -1, -1):
        for col in range(6):
            record = [True for _ in range(6)]
            connect = bfs(board, record, row, col)
            if len(connect) >= 3:
                return connect
    return -1


def bfs(board, record, row, col):
    queue = deque([row, col])
    connect = [[row, col]]
    record[row][col] = False

    color = board[row, col]

    while queue:
        cur = queue.popleft()
        row = cur[0]
        col = cur[1]
        #     위
        if row - 1 >= 0 and board[row - 1, col] == color and record[
            row - 1, col]:
            queue.append([row - 1, col])
            connect = [[row - 1, col]]
            record[row - 1][col] = False
        #     아래
        if row + 1 <= 5 and board[row + 1, col] == color and record[
            row + 1, col]:
            queue.append([row + 1, col])
            connect = [[row + 1, col]]
            record[row + 1][col] = False
        #     왼쪽
        if col - 1 >= 0 and board[row, col - 1] == color and record[
            row, col - 1]:
            queue.append([row, col - 1])
            connect = [[row, col - 1]]
            record[row][col - 1] = False
        #     오른쪽
        if col + 1 <= 5 and board[row, col + 1] == color and record[
            row, col + 1]:
            queue.append([row, col + 1])
            connect = [[row, col + 1]]
            record[row][col + 1] = False

    return connect

solution([[1,1],[2,1],[1,2],[3,3],[6,4],[3,1],[3,3],[3,3],[3,4],[2,1]])
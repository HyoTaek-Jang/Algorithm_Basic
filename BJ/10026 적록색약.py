from collections import deque
import copy


def bfs(board, isAmblyopia, pos):
    queue = deque()
    queue.append([pos[0], pos[1], board[pos[0]][pos[1]]])
    board[pos[0]][pos[1]] = "X"

    while queue:
        current = queue.popleft()
        for move in moves:
            new_row = current[0] + move[0]
            new_col = current[1] + move[1]
            if not (0 <= new_row < len(board) and 0 <= new_col < len(board[new_row])):
                continue
            if isAmblyopia and not amblyopiaColor(board[new_row][new_col], current[2]):
                continue
            elif not isAmblyopia and board[new_row][new_col] != current[2]:
                continue
            elif board[new_row][new_col] == "X":
                continue
            queue.append([new_row, new_col, current[2]])
            board[new_row][new_col] = "X"

    return board


def amblyopiaColor(a, b):
    if a == "B":
        return a == b
    if b == "B":
        return False
    return True


def makeAnswer(board, isAmblyopia):
    count = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == "X":
                continue
            count += 1
            board = bfs(board, isAmblyopia, [row, col])

    return count


N = int(input())
board = []
for _ in range(N):
    board.append(list(input()))
amblyopiaBoard = copy.deepcopy(board)

moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]

nomal = makeAnswer(board, False)
amblyopia = makeAnswer(amblyopiaBoard, True)

print(nomal, amblyopia)

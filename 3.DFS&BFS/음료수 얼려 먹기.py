from collections import deque

def solution():
    N, M = map(int, input().split())

    board = []
    for _ in range(N):
        board.append(list(map(int,list(input()))))

    checkBoard = [[True] * M for _ in range(N)]
    moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    queue = deque()
    answer = 0
    for row in range(N):
        for col in range(M):
            if board[row][col] == 0 and checkBoard[row][col] == True:
                answer += 1
                queue.append([row, col])
                checkBoard[row][col] = False
                while queue:
                    current = queue.popleft()
                    for move in moves:
                        if not(0 <= current[0]+move[0] < N and 0 <= current[1] + move[1] < M):
                            continue
                        if board[current[0] + move[0]][current[1] + move[1]] == 0 and checkBoard[current[0] + move[0]][current[1] + move[1]] == True:
                            queue.append([current[0] + move[0],current[1] + move[1]])
                            checkBoard[current[0] + move[0]][current[1] + move[1]] = False

    print(answer)


solution()
import math
from collections import deque


def solution():
    N, M = map(int, input().split())

    board, answer = [], []
    INF = math.inf
    for _ in range(N):
        board.append(list(map(int, input())))
        answer.append([INF] * M)
    answer[0][0] = 1

    moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    queue = deque()
    queue.append([0,0])
    while queue:
        current = queue.popleft()

        for move in moves:
            if not (0 <= current[0] + move[0] < N and 0 <= current[1] + move[1] < M) or board[current[0] + move[0]][current[1] + move[1]] == 0:
                continue
            if answer[current[0] + move[0]][current[1] + move[1]] > answer[current[0]][current[1]] + 1:
                answer[current[0] + move[0]][current[1] + move[1]] = answer[current[0]][current[1]] + 1
                queue.append([current[0] + move[0], current[1] + move[1]])

    print(answer[N - 1][M - 1])


solution()

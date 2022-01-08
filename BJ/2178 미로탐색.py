from collections import deque

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

queue = deque()
queue.append([0, 0, 1])
board[0][0] = '0'
moves = [[-1, 0], [0, -1], [0, 1], [1, 0]]

while queue:
    cur = queue.popleft()
    if cur[0] == N-1 and cur[1] == M-1:
        print(cur[2])
        break
    for move in moves:
        new_r = cur[0] + move[0]
        new_c = cur[1] + move[1]
        if 0 <= new_r < N and 0 <= new_c < M and board[new_r][new_c] == '1':
            queue.append([new_r, new_c, cur[2] + 1])
            board[new_r][new_c] = '0'


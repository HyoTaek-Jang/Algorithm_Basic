from collections import deque


def solution(m, n, puddles):
    board = [[1e9] * m for _ in range(n)]
    dp = [[0] * m for _ in range(n)]
    for p in puddles:
        if len(p) == 0:
            break
        board[p[1] - 1][p[0] - 1] = -1

    moves = [[0, 1], [1, 0]]
    queue = deque()
    queue.append([0, 0])
    board[0][0] = 0
    dp[0][0] = 1

    while queue:
        cur = queue.popleft()
        for move in moves:
            new_r = cur[0] + move[0]
            new_c = cur[1] + move[1]
            if new_r < n and new_c < m and board[new_r][new_c] != -1:
                if board[new_r][new_c] == board[cur[0]][cur[1]] + 1:
                    dp[new_r][new_c] += dp[cur[0]][cur[1]]
                elif board[new_r][new_c] > board[cur[0]][cur[1]] + 1:
                    dp[new_r][new_c] = dp[cur[0]][cur[1]]
                    board[new_r][new_c] = board[cur[0]][cur[1]] + 1
                    queue.append([new_r, new_c])

    return dp[n - 1][m - 1] % 1000000007
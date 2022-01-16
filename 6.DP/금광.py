N, M = map(int, input().split())
array = list(map(int, input().split()))
board = []
board_dp = [[-1] * M for _ in range(N)]
for i in range(N):
    board.append(array[i*M:i*M+M])
    board_dp[i][0] = board[i][0]

moves = [[-1,-1], [0,-1], [1,-1]]

for col in range(1, M):
    for row in range(N):
        for move in moves:
            new_r = row + move[0]
            new_c = col + move[1]

            if 0 <= new_c < M and 0 <= new_r < N:
                board_dp[row][col] = max(board_dp[new_r][new_c] + board[row][col], board_dp[row][col])

answer = 0
for row in range(N):
    answer = max(answer, board_dp[row][M-1])
print(answer)

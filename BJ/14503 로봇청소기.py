N, M = map(int, input().split())
r, c, command = map(int, input().split())

# 0 : 빈 칸, 1 : 벽, 2: 청소 끝
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

moves = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def hasBlank(r, c):
    for move in moves:
        new_r = r + move[0]
        new_c = c + move[1]
        if 0 <= new_r < N and 0 <= new_c < M and board[new_r][new_c] == 0:
            return True
    return False


answer = 0
while True:
    if board[r][c] == 0:
        board[r][c] = 2
        answer += 1
    if not hasBlank(r, c):
        new_r = r - moves[command][0]
        new_c = c - moves[command][1]
        if 0 <= new_r < N and 0 <= new_c < M and board[new_r][new_c] != 1:
            r = new_r
            c = new_c
            continue
        break
    new_command = (command - 1) % 4
    new_r = r + moves[new_command][0]
    new_c = c + moves[new_command][1]
    command = new_command
    if 0 <= new_r < N and 0 <= new_c < M and board[new_r][new_c] == 0:
        r = new_r
        c = new_c

print(answer)

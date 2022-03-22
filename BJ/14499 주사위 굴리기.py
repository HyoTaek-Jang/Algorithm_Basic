N, M, x, y, K = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

commands = list(map(int, input().split()))

dice = [0, 0, 0, 0, 0, 0]  # 뒤,왼,위,오,앞,아래
moves = [[0, 0], [0, 1], [0, -1], [-1, 0], [1, 0]]  # 동, 서 ,북 , 남


def moveDice(command, dice):
    temp_left = dice[1]
    temp_front = dice[-2]
    if command == 1:  # 동
        dice[1] = dice[-1]
        dice[-1] = dice[3]
        dice[3] = dice[2]
        dice[2] = temp_left
    if command == 2:
        dice[1] = dice[2]
        dice[2] = dice[3]
        dice[3] = dice[-1]
        dice[-1] = temp_left
    if command == 3:
        dice[-2] = dice[-1]
        dice[-1] = dice[0]
        dice[0] = dice[2]
        dice[2] = temp_front
    if command == 4:
        dice[-2] = dice[2]
        dice[2] = dice[0]
        dice[0] = dice[-1]
        dice[-1] = temp_front
    return dice


for command in commands:
    move = moves[command]
    if not (0 <= x + move[0] < N and 0 <= y + move[1] < M):
        continue
    x += move[0]
    y += move[1]

    dice = moveDice(command, dice)
    if board[x][y] == 0:
        board[x][y] = dice[-1]
    else:
        dice[-1] = board[x][y]
        board[x][y] = 0

    print(dice[2])


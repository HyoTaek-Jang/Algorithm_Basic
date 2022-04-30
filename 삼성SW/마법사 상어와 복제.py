import copy

M, S = map(int, input().split())

# 0. 세팅
board = [[[0 for _ in range(8)] for _ in range(4)] for _ in range(4)]
smell = [[0 for _ in range(4)] for _ in range(4)]

fish_direction = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
for _ in range(M):
    x, y, d = map(int, input().split())
    board[x - 1][y - 1][d - 1] += 1

shark = list(map(int, input().split()))
shark[0] -= 1
shark[1] -= 1
shark_origin_move = [[-1, 0], [0, -1], [1, 0], [0, 1]]
shark_move = []


def dfs(temp):
    if len(temp) == 3:
        shark_move.append(copy.deepcopy(temp))
        return

    for idx in range(4):
        temp.append(shark_origin_move[idx])
        dfs(temp)
        temp.pop()


dfs([])


def is_available(next_row, next_col):
    # 격자 밖
    if not (0 <= next_row < 4 and 0 <= next_col < 4):
        return False

    # 상어 유무
    if shark[0] == next_row and shark[1] == next_col:
        return False

    # 물고기 냄새
    if smell[next_row][next_col] != 0:
        return False

    return True


def fish_move(position, direction, fish_cnt):
    origin_direction = direction
    cnt = 0
    while cnt <= 8:
        cur_direction = fish_direction[direction]
        next_row, next_col = position[0] + cur_direction[0], position[1] + cur_direction[1]
        if is_available(next_row, next_col):
            board[position[0]][position[1]][origin_direction] -= fish_cnt
            board[next_row][next_col][direction] += fish_cnt
            break
        else:
            cnt += 1
            direction = (direction - 1) % 8


def shark_dfs(position):
    decide_board = board
    decide_cnt = -1
    last_position = shark
    decide_smell = smell

    for moves in shark_move:
        cnt = 0
        row = position[0]
        col = position[1]
        flag = False
        temp_board = copy.deepcopy(board)
        temp_smell = copy.deepcopy(smell)

        for move in moves:
            row += move[0]
            col += move[1]
            if not (0 <= row < 4 and 0 <= col < 4):
                flag = True
                break
            if sum(board[row][col]):
                cnt += sum(temp_board[row][col])
                temp_board[row][col] = [0 for _ in range(8)]
                temp_smell[row][col] = 3

        if not flag and decide_cnt < cnt:
            last_position = [row, col]
            decide_cnt = cnt
            decide_board = temp_board
            decide_smell = temp_smell

    return decide_board, decide_smell, last_position


for _ in range(S):
    # 1. 복제 - 5번에서 추가하면 됨
    copy_temp = copy.deepcopy(board)

    # 2. 물고기 이동, 바라본 방향에 상어, 냄새, 격자 밖 x, 반시계 이동 즉, direction - 1
    for row in range(4):
        for col in range(4):
            for idx in range(8):
                if copy_temp[row][col][idx] > 0:
                    fish_move([row, col], idx, copy_temp[row][col][idx])

    # 3. 상어 이동, 상좌하우 순서 - 격자 밖 break, 가장 많은 물고기, 죽이고 smell 2로 업뎃
    board, smell, shark = shark_dfs(shark)

    # 4. 2번전 냄새 빠잉 / smell 1씩 줄이기
    for row in range(4):
        for col in range(4):
            if smell[row][col] > 0:
                smell[row][col] -= 1

    # 5. 복제
    for row in range(4):
        for col in range(4):
            for direction in range(8):
                board[row][col][direction] += copy_temp[row][col][direction]

answer = 0
for row in range(4):
    for col in range(4):
        answer += sum(board[row][col])

print(answer)

def solution():
    col, row = list(input())
    col = ord(col) - 96
    row = int(row)

    dx = [-1, 1, 2, 2, -1, 1, -2, -2]
    dy = [-2, -2, -1, 1, 2, 2, -1, 1]
    answer = 0

    for move_idx in range(8):
        if 0 < col + dx[move_idx] <= 8 and 0 < row + dy[move_idx] <= 8:
            answer += 1

    print(answer)


solution()

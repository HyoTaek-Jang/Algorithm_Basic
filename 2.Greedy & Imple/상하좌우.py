def solution():
    size = int(input())
    root = input().split()

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    move = ['L', 'R', 'U', 'D']

    x, y = 1, 1
    for cur in root:
        idx = move.index(cur)
        temp_x = x + dx[idx]
        temp_y = y + dy[idx]
        if 0 < temp_y <= size and 0 < temp_x <= size:
            x = temp_x
            y = temp_y

    print(y, x)

solution()
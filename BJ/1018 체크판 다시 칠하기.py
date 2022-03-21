import sys

si = sys.stdin

N, M = map(int, si.readline().split())
board = []

for _ in range(N):
    board.append(list(si.readline().strip()))

answer = 1e9
for idx in range(2):
    color = ['B', 'W']
    changed = [[False] * M for _ in range(N)]
    color_idx = idx
    cur_idx = color_idx
    for row in range(N):
        for col in range(M):
            if board[row][col] != color[cur_idx]:
                changed[row][col] = True
            cur_idx = (cur_idx + 1) % 2
        color_idx = (color_idx + 1) % 2
        cur_idx = color_idx

    for row in range(N - 8 + 1):
        for col in range(M - 8 + 1):
            count = 0
            for cur_row in range(row, row + 8):
                count += sum(changed[cur_row][col:col + 8])
            answer = min(count, answer)

print(answer)

import sys

si = sys.stdin

N, M = map(int, si.readline().split())
board = []
for _ in range(N):
    board.append(list(map(int, si.readline().strip().split())))

moves = [[0, 1], [1, 0], [-1, 0], [0, -1]]
shape = [[(0, 1), (-1, 1), (0, 2)], [(1, 0), (2, 0), (1, 1)], [(0, 1), (0, 2), (1, 1)], [(1, 0), (2, 0), (1, -1)]]


def dfs(count, location, value, record):
    global answer

    if count == 4:
        if answer < value:
            answer = value
        return

    for move in moves:
        new_r = location[0] + move[0]
        new_c = location[1] + move[1]

        if not (0 <= new_r < N and 0 <= new_c < M) or (new_r, new_c) in record:
            continue
        record.append((new_r, new_c))
        dfs(count + 1, [new_r, new_c], value + board[new_r][new_c], record)
        record.pop()


answer = 0
for row in range(N):
    for col in range(M):
        dfs(1, [row, col], board[row][col], [(row, col)])

        for s in shape:
            cur = board[row][col]
            for i in s:
                new_r = row + i[0]
                new_c = col + i[1]
                if not (0 <= new_r < N and 0 <= new_c < M):
                    break
                cur += board[new_r][new_c]
            answer = max(answer, cur)

print(answer)

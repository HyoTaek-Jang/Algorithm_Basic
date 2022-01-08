import sys
from collections import deque

N = int(sys.stdin.readline().strip())
location = []
answer = 0
shark_power, shark_charge = 2, 0
board = []
for row in range(N):
    cur = list(map(int, sys.stdin.readline().strip().split()))
    for col in range(len(cur)):
        if cur[col] == 9:
            location = [row, col]
            cur[col] = 0
    board.append(cur)

moves = [[-1, 0], [0, -1], [0, 1], [1, 0]]


def bfs():
    global answer, shark_charge, shark_power, location
    queue = deque()
    history = set()
    queue.append([location[0], location[1], 0])  # 행,열,거리
    history.add(tuple(location))
    candidate = []

    while queue:
        current = queue.popleft()
        distance = current[2] + 1
        # 후보군 다 모였나 확인
        if len(candidate) and distance > candidate[0][2]:
            candidate.sort(key=lambda x: (x[0], x[1]))
            shark_charge += 1
            if shark_power == shark_charge:
                shark_power += 1
                shark_charge = 0
            new_r, new_c = candidate[0][0], candidate[0][1]
            location = [new_r, new_c]
            board[new_r][new_c] = 0
            answer += candidate[0][2]
            return True

        for move in moves:
            new_r = current[0] + move[0]
            new_c = current[1] + move[1]
            if 0 <= new_r < N and 0 <= new_c < N and not (new_r, new_c) in history:
                if board[new_r][new_c] > shark_power:
                    continue
                if 0 < board[new_r][new_c] < shark_power:
                    candidate.append([new_r, new_c, distance])
                queue.append([new_r, new_c, distance])
                history.add((new_r, new_c))
    return False


while True:
    if not bfs():
        print(answer)
        break

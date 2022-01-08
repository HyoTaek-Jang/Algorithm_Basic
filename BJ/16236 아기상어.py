import sys
from collections import deque

N = int(sys.stdin.readline())
board = []
shark = []
shark_power = 2
charge = 0
answer = 0

dict = {}
for j in range(1, 7):
    dict[j] = 0
for i in range(N):
    row = list(map(int, sys.stdin.readline().strip().split()))
    for cur in row:
        for j in range(1, 7):
            if cur == j:
                dict[j] += 1
    if 9 in row:
        shark = [i, row.index(9)]
        row[row.index(9)] = 0
    board.append(row)

moves = [[-1, 0], [0, -1], [0, 1], [1, 0]]


def bfs():
    global shark, answer, shark_power, charge
    queue = deque()
    history = set()
    history.add(tuple(shark))
    queue.append([shark[0], shark[1], 0])
    candidate = []
    while queue:
        current = queue.popleft()
        distance = current[2] + 1
        if len(candidate) and dict[board[candidate[0][0]][candidate[0][1]]] == len(candidate):
            candidate.sort(key=lambda x: (-x[0], x[1]))
            charge += 1
            if charge == shark_power:
                shark_power += 1
                charge = 0
            shark = [candidate[0][0], candidate[0][1]]
            dict[board[candidate[0][0]][candidate[0][1]]] -= 1
            board[candidate[0][0]][candidate[0][1]] = 0
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

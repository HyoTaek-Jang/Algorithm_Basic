import sys
from collections import deque

si = sys.stdin

N = int(si.readline())  # 보드
board = [[0] * N for _ in range(N)]  # 0 : 빈 것, 1 : 사과

K = int(si.readline())  # 사과 개수
for _ in range(K):
    row, col = map(int, si.readline().split())
    board[row - 1][col - 1] = 1

L = int(si.readline())  # 방향 변환 횟수
queue = deque()  # 방향 변경
for _ in range(L):
    queue.append(list(si.readline().strip().split()))

moves = [[0, 1], [-1, 0], [0, -1], [1, 0]]  # 우, 상, 좌, 하

d_cnt = 120
direction = moves[0]  # 초기 방향, 우측
cur_change = queue.popleft()

head = [0, 0]
tail = [0, 0]
time = 0
record = deque()
while True:
    time += 1
    record.append((head[0], head[1]))
    head = [head[0]+direction[0], head[1]+direction[1]]
    if cur_change[0] == str(time):
        if cur_change[1] == "L":
            d_cnt += 1
        elif cur_change[1] == "D":
            d_cnt -= 1
        direction = moves[d_cnt % 4]
        if queue:
            cur_change = queue.popleft()

    if not (0 <= head[0] < N and 0 <= head[1] < N):
        break
    if (head[0], head[1]) in record:
        break

    # 꼬리 이동
    if board[head[0]][head[1]] == 1:
        board[head[0]][head[1]] = 0
    else:
        record.popleft()



print(time)

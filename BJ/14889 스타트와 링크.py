import sys

N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().strip().split())))

history = [True] * N
def dfs(min_value, cnt, idx):
    if cnt == N // 2:
        start, link = 0, 0
        for j in range(N):
            for k in range(N):
                if not history[j] and not history[k]:
                    start += board[j][k]
                elif history[j] and history[k]:
                    link += board[j][k]
        return min(min_value, abs(start - link))

    for i in range(idx, N):
        if history[i]:
            history[i] = False
            min_value = min(dfs(min_value, cnt + 1, i+1), min_value)
            history[i] = True

    return min_value


print(dfs(9e10, 0, 0))

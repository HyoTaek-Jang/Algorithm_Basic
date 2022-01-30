from collections import deque


def solution(n, edge):
    visited = [True] * n
    board = [1e9] * n
    graph = [[] for _ in range(n)]
    for e in edge:
        graph[e[0] - 1].append(e[1] - 1)
        graph[e[1] - 1].append(e[0] - 1)

    queue = deque()

    queue.append([0, 0])
    while queue:
        cur = queue.popleft()
        if visited[cur[0]]:
            board[cur[0]] = cur[1]
            visited[cur[0]] = False
            for i in graph[cur[0]]:
                if visited[i]:
                    board[i] = cur[1] + 1
                    queue.append([i, cur[1] + 1])

    answer = 0
    max_value = -1
    for cur in board:
        if cur == max_value:
            answer += 1
        elif cur > max_value:
            max_value = cur
            answer = 1

    return answer


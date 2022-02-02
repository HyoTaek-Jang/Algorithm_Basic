from collections import deque

def solution(n, results):
    win = {}
    lose = {}
    for i in range(1, n + 1):
        win[i] = []
        lose[i] = []

    for r in results:
        win[r[0]].append(r[1])
        lose[r[1]].append(r[0])

    answer = 0
    for cur in range(1, n + 1):
        visited = [True] * (n + 1)
        visited = out(visited, win, cur)
        visited = out(visited, lose, cur)

        if sum(visited) == 2:
            answer += 1

    return answer


def out(visited, win, target):
    queue = deque()
    for i in win[target]:
        if visited[i]:
            queue.append(i)
            visited[i] = False

    while queue:
        cur = queue.popleft()
        for i in win[cur]:
            if visited[i]:
                queue.append(i)
                visited[i] = False

    return visited

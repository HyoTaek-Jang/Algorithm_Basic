from collections import deque

V = int(input())
node_dict = {}
for i in range(V+1):
    node_dict[i] = {}
for _ in range(V - 1):
    current = list(map(int, input().split()))
    node_dict[current[0]][current[1]] = current[2]
    node_dict[current[1]][current[0]] = current[2]


def bfs(start):
    queue = deque()
    visited = [True] * (V + 1)
    value = [0] * (V + 1)

    queue.append(start)
    visited[start] = False
    while queue:
        cur = queue.popleft()
        for i in node_dict[cur]:
            if visited[i]:
                queue.append(i)
                visited[i] = False
                value[i] = max(value[cur] + node_dict[cur][i], value[i])

    return value


first = bfs(1)
idx = first.index(max(first))
answer = bfs(idx)

print(max(answer))

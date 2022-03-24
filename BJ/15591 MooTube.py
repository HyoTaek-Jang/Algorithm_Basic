import sys
from collections import deque

si = sys.stdin

N, Q = map(int, si.readline().split())
table = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    p, q, r = map(int, si.readline().split())
    table[p].append((q, r))
    table[q].append((p, r))

for _ in range(Q):
    k, v = map(int, si.readline().split())
    queue = deque()
    queue.append((v, 1e9))
    visited = [False] * (N+1)
    visited[v] = True

    answer = 0
    while queue:
        current, cur_value = queue.popleft() # current position
        for dest, value in table[current]:
            if visited[dest]:
                continue
            min_value = min(cur_value, value)
            queue.append((dest, min_value))
            if min_value >= k:
                answer += 1
            visited[dest] = True

    print(answer)



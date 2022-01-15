import sys
from collections import deque

N, M = map(int, sys.stdin.readline().strip().split())

connection = {}
for i in range(N):
    connection[i+1] = []

for _ in range(M):
    src, dest = map(int, sys.stdin.readline().strip().split())
    connection[src].append(dest)
    connection[dest].append(src)

history = [1] * (N+1)
history[0] = 0

def bfs(start):
    queue = deque()
    queue.append(start)
    history[start] = 0

    while queue:
        current = queue.popleft()

        for i in connection[current]:
            if history[i]:
                queue.append(i)
                history[i] = 0

answer = 0
while sum(history) != 0:
    for i in range(N+1):
        if history[i]:
            bfs(i)
            answer += 1
            break

print(answer)
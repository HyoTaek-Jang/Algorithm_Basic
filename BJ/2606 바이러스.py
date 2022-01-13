import sys
from collections import deque

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
connection = {}
for i in range(N+1):
    connection[i] = []
for _ in range(M):
    src, dest = map(int, sys.stdin.readline().strip().split())
    connection[src].append(dest)
    connection[dest].append(src)

history = []

answer = 0
def bfs(start):
    global answer
    queue = deque()
    queue.append(start)
    history.append(start)
    while queue:
        current = queue.popleft()
        for i in connection[current]:
            if i not in history:
                answer += 1
                history.append(i)
                queue.append(i)

bfs(1)
print(answer)
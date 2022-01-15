import sys
from collections import deque

K = int(sys.stdin.readline())
forSum = deque()

for _ in range(K):
    cur = int(sys.stdin.readline())
    if cur == 0 and forSum:
        forSum.pop()
    if cur != 0:
        forSum.append(cur)

print(sum(forSum))
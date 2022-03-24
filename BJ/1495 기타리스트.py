import sys
from collections import deque

si = sys.stdin

N, S, M = map(int, si.readline().split())
V = list(map(int, si.readline().strip().split()))

answer = -1
history = set()
queue = deque()
queue.append((S, 0)) # 현재 볼륨, 바꿀 인덱스

while queue:
    c_vol, c_idx = queue.popleft()

    if c_idx == N:
        answer = max(answer, c_vol)
        continue
    if 0 <= c_vol + V[c_idx] <= M and (c_vol + V[c_idx], c_idx + 1) not in history:
        history.add((c_vol + V[c_idx], c_idx + 1))
        queue.append((c_vol + V[c_idx], c_idx + 1))
    if 0 <= c_vol - V[c_idx] <= M and (c_vol - V[c_idx], c_idx + 1) not in history:
        history.add((c_vol - V[c_idx], c_idx + 1))
        queue.append((c_vol - V[c_idx], c_idx + 1))

print(answer)

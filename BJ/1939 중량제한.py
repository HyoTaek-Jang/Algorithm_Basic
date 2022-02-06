import sys
from collections import deque
import heapq

si = sys.stdin

N, M = map(int, si.readline().split())

table = {}
for i in range(1, N + 1):
    table[i] = []

for _ in range(M):
    A, B, C = map(int, si.readline().split())
    table[A].append([B, C])
    table[B].append([A, C])

start, end = map(int, si.readline().split())

possible = [0] * (N + 1)
possible[start] = 2e9
pq = []
heapq.heappush(pq, [0, start])

while pq:
    weight, dest = heapq.heappop(pq)
    weight *= -1

    if dest != start and possible[dest] > weight:
        continue

    for next_dest, next_weight in table[dest]:
        if possible[dest] < next_weight:
            next_weight = possible[dest]
        if possible[next_dest] < next_weight:
            possible[next_dest] = next_weight
            heapq.heappush(pq, [-next_weight, next_dest])

print(possible[end])

import sys
import heapq

V = int(sys.stdin.readline())
E = int(sys.stdin.readline())

table = {}
for _ in range(E):
    cur = list(map(int, sys.stdin.readline().strip().split()))
    if not cur[0] in table:
        table[cur[0]] = []
    table[cur[0]].append([cur[1], cur[2]])

start, destination = map(int, sys.stdin.readline().strip().split())

distance = [1e9] * (V + 1)
distance[start] = 0

pq = []
heapq.heappush(pq, [0, start])  # 거리, 도착지

while pq:
    weight, dest = heapq.heappop(pq)

    if distance[dest] < weight:
        continue

    if dest in table:
        for cur in table[dest]:
            if weight + cur[1] < distance[cur[0]]:
                distance[cur[0]] = weight + cur[1]
                heapq.heappush(pq, [weight + cur[1], cur[0]])

print(distance[destination])

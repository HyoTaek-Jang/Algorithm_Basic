import sys
import heapq

N, M, X = map(int, sys.stdin.readline().split())

table = {}
for _ in range(M):
    start, end, weight = map(int, sys.stdin.readline().split())
    if not start in table:
        table[start] = []
    table[start].append([end, weight])


def dijkstra(start):
    distance = [1e9] * (N + 1)
    pq = []
    distance[start] = 0
    heapq.heappush(pq, [0, start])

    while pq:
        dist, point = heapq.heappop(pq)

        if distance[point] < dist:
            continue

        if point in table:
            for dest, weight in table[point]:
                if distance[dest] > weight + dist:
                    distance[dest] = weight + dist
                    heapq.heappush(pq, [weight + dist, dest])

    return distance


board = [[0] * (N + 1)]
for i in range(1, N + 1):
    board.append(dijkstra(i))

answer = []
for i in range(1, N + 1):
    answer.append(board[i][X] + board[X][i])

print(max(answer))

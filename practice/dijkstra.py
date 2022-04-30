import heapq

# 현재 방문하지 않은 노드에서 최소 값을 갈 수 있는 곳으로 이동
# 방문 처리 및 연관된 값 변경

def dijkstra(table, start):
    pq = [(0, start)]
    distance = [1e9] * len(table)
    distance[start] = 0

    while pq:
        cur_distance, cur_node = heapq.heappop(pq)

        if cur_distance > distance[cur_node]:
            continue

        for next_node, next_distance in table[cur_node]:
            if distance[next_node] > cur_distance + next_distance:
                distance[next_node] = cur_distance + next_distance
                heapq.heappush(pq, (distance[next_node], next_node))

    return distance


n, m = map(int, input().split())

# start : 시작노드
start = int(input())

# 노드정보
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split()) # a -> b (비용 c)
    graph[a].append((b, c))

print(dijkstra(graph, start))

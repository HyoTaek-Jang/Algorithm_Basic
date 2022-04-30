from collections import deque


#
# def bfs(graph, start):
#     visited = set()
#     queue = deque()
#     queue.append(start)
#     visited.add(start)
#
#     while queue:
#         current = queue.popleft()
#         print(current)
#
#         for i in graph[current]:
#             if i not in visited:
#                 queue.append(i)
#                 visited.add(i)

def bfs(graph, start):
    visited = set()
    queue = deque()

    queue.append(start)
    visited.add(start)

    while queue:
        current = queue.popleft()
        print(current)

        for connect in graph[current]:
            if connect not in visited:
                queue.append(connect)
                visited.add(connect)


bfs({
    'A': ['B'],
    'B': ['A', 'C', 'H'],
    'C': ['B', 'D'],
    'D': ['C', 'E', 'G'],
    'E': ['D', 'F'],
    'F': ['E'],
    'G': ['D'],
    'H': ['B', 'I', 'J', 'M'],
    'I': ['H'],
    'J': ['H', 'K'],
    'K': ['J', 'L'],
    'L': ['K'],
    'M': ['H']
}, 'A')

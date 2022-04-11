def dfs(graph, start):
    visited = set()
    stack = [start]
    visited.add(start)

    while stack:
        current = stack.pop()
        print(current)
        for i in graph[current]:
            if i not in visited:
                visited.add(i)
                stack.append(i)


dfs({
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

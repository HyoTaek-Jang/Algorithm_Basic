'''
BFS breadth first search
너비 우선 탐색, 가까운 노드부터 우선적으로 탐색하는 알고리즘.
큐 자료구조를 활용
'''
from collections import deque

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7],
]

visited = [False] * 9


def BFS(graph, node, visited):
    queue = deque([node])
    visited[node] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


# BFS(graph, 1, visited)


def maze():
    row, col = map(int, input().split(' '))
    board = []

    for i in range(row):
        rowData = input()
        rowList = [a for a in rowData]
        board.append(list(
            map(lambda x: 1 if x == "1" else 0, rowList)))

    count = mazeCheck(board, 0, 0)

    print(count)

def mazeCheck(board, i, v):
    if i==len(board)-1 and v==len(board[0])-1:
        return board[i][v]

    try:
        if board[i + 1][v] == 1:
            board[i + 1][v] = board[i][v] + 1
            return mazeCheck(board, i + 1, v)
    except IndexError:
        pass
    try:
        if board[i][v + 1] == 1:
            board[i][v + 1] = board[i][v] + 1
            return mazeCheck(board, i, v + 1)
    except IndexError:
        pass
    try:
        if board[i][v - 1] == 1:
            board[i][v - 1] = board[i][v] + 1
            return mazeCheck(board, i, v - 1)
    except IndexError:
        pass
    try:
        if board[i - 1][v] == 1:
            board[i - 1][v] = board[i][v] + 1
            mazeCheck(board, i - 1, v)
    except IndexError:
        pass


maze()

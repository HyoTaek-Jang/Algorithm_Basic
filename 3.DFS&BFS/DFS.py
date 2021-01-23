'''
DFS, BFS는 그래프 탐색 알고리즘
자주 등장하는 유형
'''
from collections import deque

'''
스택 : 선입후출
입구와 출구가 동일한 형태.
리스트 사용
append 마지막에 추가

스택 : 선입선출.
입구와 출구가 모두 뚫린 터널 형태
deque(뎁) 라이브러리 사용.
popleft 왼쪽거 빼냄.
reverse있음
'''

'''
재귀함수 자기 자신을 다시 호출하는 함수! 
직관적이고 간결해짐!

최대공약수(GCD) 구하기
복잡한 알고리즘을 간결하게 작성할 수 있음. 모든 재귀는 반복문으로 구현 가능.
스택 라이브러리 대신에 재귀 함수를 이용하기도 함.
'''

'''
DFS Depth - First Search 깊이 우선 탐색
가장 깊게 들어갔다가 갈 곳이 없으면 나오는 거!
스택이나 재귀함수를 이용
'''
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


def DFS(graph, node, visited):
    visited[node] = True
    print(node, end=' ')
    for i in graph[node]:
        if visited[i] == False:
            DFS(graph, i, visited)


# DFS(graph, 1, visited)

def icecream():
    row, col = map(int, input().split(' '))
    board = []
    count = 0

    for i in range(row):
        board.append(list(
            map(lambda x: True if x == "0" else False, input().split(' '))))

    for i in range(row):
        for v in range(col):
            if board[i][v]:
                count += 1
                board[i][v] == False
                nearCheck(board, i, v)
    print(count)


def nearCheck(board, i, v):
    try:
        if board[i + 1][v]:
            board[i + 1][v] = False
            nearCheck(board, i + 1, v)
    except IndexError:
        pass
    try:
        if board[i][v + 1]:
            board[i][v + 1] = False
            nearCheck(board, i, v + 1)
    except IndexError:
        pass

# icecream()

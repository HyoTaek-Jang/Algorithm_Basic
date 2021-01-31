'''
DFS, BFS는 그래프 탐색 알고리즘
자주 등장하는 유형
'''
import copy
from collections import deque
from itertools import permutations, combinations

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

# 백준 14502번 연구소
# 시부레 진짜 아오 너무 힘드네
# 처음엔 어케 벽을 막을까 고민하다가 그냥 모든 경우에서 max를 구하는거로 변경


def virus():
    N, M = map(int, input().split(' '))

    room = []
    idx = []
    count = []
    for i in range(N):
        row = list(map(int, input().split(' ')))
        room.append(row)
        for j in range(M):
            if room[i][j] == 0:
                idx.append((i, j))

    combiIdx = list(combinations(idx, 3))

    for k in range(len(combiIdx)):
        copyRoom = copy.deepcopy(room)
        goLoop = True
        for i in range(3):
            if copyRoom[combiIdx[k][i][0]][combiIdx[k][i][1]] != 0:
                goLoop = False
                break
            copyRoom[combiIdx[k][i][0]][combiIdx[k][i][1]] = 1

        if goLoop:
            for i in range(N):
                for j in range(M):
                    if copyRoom[i][j] == 2:
                        copyRoom[i][j] = 3
                        infection((i, j), copyRoom)
            count.append(sum([row.count(0) for row in copyRoom]))

    print(max(count))


def infection(idx, room):
    try:
        newIdx = (idx[0] + 1, idx[1])
        if room[newIdx[0]][newIdx[1]] == 0 and newIdx[0] >= 0 and newIdx[
            1] >= 0:
            room[newIdx[0]][newIdx[1]] = 3
            infection(newIdx, room)
    except IndexError:
        pass
    try:
        newIdx = (idx[0] - 1, idx[1])
        if room[newIdx[0]][newIdx[1]] == 0 and newIdx[0] >= 0 and newIdx[
            1] >= 0:
            room[newIdx[0]][newIdx[1]] = 3
            infection(newIdx, room)
    except IndexError:
        pass
    try:
        newIdx = (idx[0], idx[1] + 1)
        if room[newIdx[0]][newIdx[1]] == 0 and newIdx[0] >= 0 and newIdx[
            1] >= 0:
            room[newIdx[0]][newIdx[1]] = 3
            infection(newIdx, room)
    except IndexError:
        pass
    try:
        newIdx = (idx[0], idx[1] - 1)
        if room[newIdx[0]][newIdx[1]] == 0 and newIdx[0] >= 0 and newIdx[
            1] >= 0:
            room[newIdx[0]][newIdx[1]] = 3
            infection(newIdx, room)
    except IndexError:
        pass


# virus()

# 백준 단지번호 붙이기 2667번
def apratment():
    M = int(input())

    apart = []
    count = []

    for i in range(M):
        apart.append(list(map(int, [i for i in input()])))

    for i in range(M):
        for j in range(M):
            if apart[i][j] == 1:
                count.append(checkNear(apart, (i, j), 0))

    print(len(count))
    count.sort()
    for i in count:
        print(i)


def checkNear(apt, idx, count):
    movex = [0, 0, 1, -1]
    movey = [1, -1, 0, 0]
    apt[idx[0]][idx[1]] = 3
    count += 1
    for i in range(4):
        try:
            if apt[idx[0] + movey[i]][idx[1] + movex[i]] == 1 and idx[0] + \
                    movey[i] >= 0 and idx[1] + movex[i] >= 0:
                count = checkNear(apt, (idx[0] + movey[i], idx[1] + movex[i]),
                                  count)
        except IndexError:
            pass

    return count


apratment()

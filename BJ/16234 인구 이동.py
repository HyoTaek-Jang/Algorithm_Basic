import sys
from collections import deque

si = sys.stdin

N, L, R = map(int, si.readline().split())
population = []
for _ in range(N):
    population.append(list(map(int, si.readline().strip().split())))


def checkConnection(population):
    length = len(population)
    moves = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    connection = [[[] for _ in range(length)] for _ in range(length)]
    ismove = False

    for r in range(length):
        for c in range(length):
            for move in moves:
                new_r = r + move[0]
                new_c = c + move[1]
                if not (0 <= new_c < length and 0 <= new_r < length):
                    continue
                if L <= abs(population[r][c] - population[new_r][new_c]) <= R:
                    ismove = True
                    connection[r][c].append([new_r, new_c])

    return connection, ismove


def movePeople(population, connection):
    length = len(population)
    # 0 : 아직 방문 x, 1 : 방문
    visited = [[0] * length for _ in range(length)]
    for r in range(length):
        for c in range(length):
            if visited[r][c] == 0 and len(connection[r][c]):
                queue = deque()
                union = []
                value = 0
                queue.append([r, c])
                while queue:
                    cur = queue.popleft()
                    if visited[cur[0]][cur[1]] != 0:
                        continue
                    visited[cur[0]][cur[1]] = 1
                    union.append(cur)
                    value += population[cur[0]][cur[1]]
                    for con in connection[cur[0]][cur[1]]:
                        if visited[con[0]][con[1]] == 0:
                            queue.append(con)
                for cur in union:
                    population[cur[0]][cur[1]] = value // len(union)
    return population


day = 0
connection, ismove = checkConnection(population)
while (ismove):
    # 국경 오픈 및 파퓰레이션 재정리
    population = movePeople(population, connection)
    # day++
    day += 1
    ## connection, ismove 검사
    connection, ismove = checkConnection(population)

print(day)

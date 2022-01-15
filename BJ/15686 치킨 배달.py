import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().strip().split())
board = []
home = []
chicken = []

for j in range(N):
    cur = list(map(int, sys.stdin.readline().strip().split()))
    for i in range(len(cur)):
        if cur[i] == 2:
            chicken.append([j, i])
        elif cur[i] == 1:
            home.append([j, i])
    board.append(cur)


# 뺄 거
candidate = list(combinations(chicken, M))
answer = 1e9

for chickens in candidate:
    # 세팅 완료, 이후 bfs로 answer 구하기
    cur_answer = 0
    for cur in home:
        distance = 1e9
        for store in chickens:
            distance = min(distance, abs(store[0]-cur[0])+abs(store[1]-cur[1]))
        cur_answer += distance
    answer = min(answer, cur_answer)

print(answer)

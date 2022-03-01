import sys

si = sys.stdin

N = int(si.readline())
like = {}
table = [[0] * N for _ in range(N)]

moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]
for _ in range(N ** 2):
    # 좋아하는 사람, 비어있는 칸, 위치[r,c]
    change = [0, 0, [-1, -1]]

    temp = list(map(int, si.readline().strip().split()))
    like[temp[0]] = temp[1:]

    for r in range(N):
        for c in range(N):
            if table[r][c] != 0:
                continue
            rank = [0, 0, [r, c]]
            for move in moves:
                new_r = r + move[0]
                new_c = c + move[1]
                if not (0 <= new_r < N and 0 <= new_c < N):
                    continue

                if table[new_r][new_c] == 0:
                    rank[1] += 1
                elif table[new_r][new_c] in temp[1:]:
                    rank[0] += 1

            if change[0] < rank[0]:
                change = rank
            elif change[0] == rank[0] and change[1] < rank[1]:
                change = rank
            elif change[2] == [-1, -1]:
                change = rank

    table[change[2][0]][change[2][1]] = temp[0]

answer = 0
score = [0, 1, 10, 100, 1000]
for r in range(N):
    for c in range(N):
        cnt = 0
        for move in moves:
            new_r = r + move[0]
            new_c = c + move[1]
            if not (0 <= new_r < N and 0 <= new_c < N):
                continue
            if table[r][c] in like and table[new_r][new_c] in like[table[r][c]]:
                cnt += 1
        answer += score[cnt]

print(answer)
print(table)